from flask import Flask, Blueprint, render_template, request
from langchain.vectorstores.chroma import Chroma
from dotenv import load_dotenv
from langchain.chains import RetrievalQAWithSourcesChain, RetrievalQA
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.embeddings.huggingface import HuggingFaceEmbeddings    
import os
from langchain import hub


load_dotenv()

openai_api_key=os.getenv("OPENAI_API_KEY")
embeddings=HuggingFaceEmbeddings()
db=Chroma(
            persist_directory="vs/huggingface2",
            embedding_function=embeddings
        )


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=['GET', 'POST'])
def answer():
    if request.method == 'POST':
        # retriever=db.as_retriever() #해당 데이터베이스를 retriever로 설정
        question = request.form.get('question')
        docs = db.similarity_search_with_score(question)
        relevant_docs=[]
        for doc in docs:
            relevant_docs.append({doc[1]: doc[0].page_content})
        print(relevant_docs)
        return render_template('answer.html', question=question, relevant_docs=relevant_docs)
    
    return render_template('main.html')