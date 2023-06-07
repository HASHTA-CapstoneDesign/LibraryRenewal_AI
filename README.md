# LibraryRenewal_AI

## Deployment url
> **프론트 서버** : [http://34.64.215.230:3000/](http://34.64.215.230:3000/)<br>
> **백엔드 서버** : [http://34.64.215.230:8080/](http://34.64.215.230:8080/)<br>
> **AI 서버** : http://34.64.215.230:5000/ (벡엔드와 소통하는 포트라 따로 포트를 열어두지 않았습니다.)

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FVoluntain-SKKU%2FLibraryRenewal_backend&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

### Development
![python](https://img.shields.io/badge/python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![flask](https://img.shields.io/badge/flask-000000.svg?style=for-the-badge&logo=flask&logoColor=white)
![googlecloud](https://img.shields.io/badge/googlecloud-4285F4.svg?style=for-the-badge&logo=googlecloud&logoColor=white)

## Dependencies
- pandas
- pickle
- konlpy
- sklearn
- openai
- gpt_index
- PyPDF2
- PyCryptodome
- gradio

## API
- Chat gpt API

## Function
### 책 추천 알고리즘
책 소개에서 명사만 가지고 와 코사인 유사도를 구하고 이를 정렬하여 유사도가 높은 순으로 추천해 줌
![image](https://github.com/HASHTA-CapstoneDesign/LibraryRenewal_AI/assets/112682489/77fa8dff-fdb7-4c1c-834e-c248d8768743)

### CHAT GPT를 이용한 CHATBOT
CHAT GPT에 한림대 도서관에 관한 데이터를 사전학습하여 한림대 도서관에서만 사용할 수 있는 CHATBOT 생성
![image](https://github.com/HASHTA-CapstoneDesign/LibraryRenewal_AI/assets/112682489/477a575b-ab46-47f9-af0b-b89768a3d03d)
