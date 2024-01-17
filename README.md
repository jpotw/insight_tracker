
# 개요
1. upload_views.py에서 txt파일을 업로드하고 버튼을 누른다. -> embed.py에서 huggingface embedding을 이용해 split한 text 뭉치들을 벡터화하여 저장한다.
2. OpenAI Embedding, RetrievalQA()를 통해 질문을 벡터화하고 가장 유사한 문서 10개 중 3개를 선별하여 그 내용을 바탕으로 답변을 하도록 한다.

---

# flask run 실행시 (example) :

![image](https://github.com/jpotw/insight_tracker/assets/105954991/8ea3eb5f-3928-488f-aab0-762fa7577696)


![image](https://github.com/jpotw/insight_tracker/assets/105954991/cb27ea84-cdeb-49bb-b627-756901e0efc7)
