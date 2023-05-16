import pandas as pd
import pickle
from konlpy.tag import *
from sklearn.feature_extraction.text import TfidfVectorizer

traindata = pd.read_csv("fainl.csv")

dataset = traindata.loc[:, ['ISBN_THIRTEEN_NO']]
dataset = dataset.astype({'ISBN_THIRTEEN_NO':'str'})

pickle.dump(dataset, open('bookDataISBN.pickle','wb'))

comment = traindata['BOOK_INTRCN_CN']
comment = comment.values.tolist()
print(type(comment))

okt = Okt()

def morph(input_data) : #형태소 분석
    preprocessed1 = okt.nouns(input_data)
    # result = [word for word in preprocessed1 if not word in stop_words]
    return ' '.join(preprocessed1)

result = []
for i in range(len(comment)) :
  result.append(morph(comment[i]))

tfidfv = TfidfVectorizer().fit(result)
print(tfidfv.transform(result).toarray())
tfidf_matrix = tfidfv.transform(result).toarray()
print(tfidfv.vocabulary_)

from sklearn.metrics.pairwise import cosine_similarity

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print('코사인 유사도 연산 결과 :',cosine_sim.shape)

pickle.dump(cosine_sim, open('cosine_sim.pickle','wb'))