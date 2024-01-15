
# 개요

1. embed.py에서 huggingface embedding을 이용해 split한 text 뭉치들을 벡터화하여 저장한다.
2. OpenAI Embedding, RetrievalQA()를 통해 질문을 벡터화하고 가장 유사한 문서 10개 중 3개를 선별하여 그 내용을 바탕으로 답변을 하도록 한다.

---

# flask run 실행시 (example) :

![image](https://github.com/jpotw/insight_tracker/assets/105954991/8ea3eb5f-3928-488f-aab0-762fa7577696)


![image](https://github.com/jpotw/insight_tracker/assets/105954991/cb27ea84-cdeb-49bb-b627-756901e0efc7)



# 문제:
1. relevant document라고 뽑은 게 전혀 관련성이 없다. 심지어 똑같은 단어를 써도 안 나온다.

          - 1) Huggingface Embedding 성능이 별로여서 or
          - 2) 방대한 문서를 "stuff"방식을 써서 중 하나인듯.


2. ai는 전혀 관련 문서를 참조하고 있지 않다.(RAG가 제대로 안 되고 있음) 그냥 chatgpt api를 써서 답변한다. 

          - 1) 관련 문서가 관련성이 없어서  
          - 2) RAG 자체가 안 되고 있거나
