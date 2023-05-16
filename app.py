import enum
import re
from gpt_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import gradio as gr
import sys
import os
from flask import Flask, request
import pickle

import json
from django.core.exceptions import ImproperlyConfigured

with open("secret.json") as f:
    secrets = json.loads(f.read())


# Keep secret keys in secrets.json
def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

CHATGPT_API = get_secret("chatgpt_api")

os.environ["OPENAI_API_KEY"] = CHATGPT_API

def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-davinci-003", max_tokens=num_outputs))

    documents = SimpleDirectoryReader(directory_path).load_data()

    index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    index.save_to_disk('index.json')

    return index

def chatbot(input_text):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(input_text, response_mode="compact")
    return response.response

iface = gr.Interface(fn=chatbot,
                     inputs=gr.inputs.Textbox(lines=7, label="Enter your text"),
                     outputs="text",
                     title="My AI Chatbot")

index = construct_index("docs")

app = Flask(__name__)

book = pickle.load(open('data/bookDataISBN.pickle', 'rb'))
cosine_sim = pickle.load(open('data/cosine_sim.pickle', 'rb'))

bookslist = []
def get_recommendations(isbn):
    # 영화 제목을 통해서 전체 데이터 기준 그 영화의 index 값을 얻기
    idx = book[book['ISBN_THIRTEEN_NO'] == isbn].index[0]

    # 코사인 유사도 매트릭스 (cosine_sim) 에서 idx 에 해당하는 데이터를 (idx, 유사도) 형태로 얻기
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 코사인 유사도 기준으로 내림차순 정렬
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # 자기 자신을 제외한 10개의 추천 영화를 슬라이싱
    sim_scores = sim_scores[1:11]
    
    # 추천 영화 목록 10개의 인덱스 정보 추출
    book_indices = [i[0] for i in sim_scores]

    isbn_list = book['ISBN_THIRTEEN_NO'].iloc[book_indices]
    
    return isbn_list

@app.route('/chatbot/')
def chat_pgt():
    input = request.args.to_dict()["input"]
    return chatbot(input)

@app.route('/recommend/')
def book_recommend():
    input = request.args.to_dict()["input"]
    return str(get_recommendations(input))

app.run()