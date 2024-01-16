from flask import Flask, render_template, request, Blueprint
from vs.models import FileUploadForm
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders.text import TextLoader
from langchain.text_splitter import CharacterTextSplitter
# from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings.huggingface import HuggingFaceEmbeddings    
from dotenv import load_dotenv
import tempfile #TextLoader expects a file path 끝나고 삭제하게 세팅
import os


load_dotenv()
inference_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

model_name="jhgan/ko-sbert-nli"
model_kwargs= {'device': 'cpu'}
encode_kwargs={'normalize_embeddings': True}
hf = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size = 600,
    chunk_overlap  = 0,
    length_function = len,
    is_separator_regex = False,
)

bp = Blueprint('upload', __name__, url_prefix='/')    

@bp.route('/', methods=['GET', 'POST'])
def upload_file():
    form = FileUploadForm()
    if request.method == 'POST' and form.validate_on_submit():
        uploaded_file = form.file.data
        if uploaded_file:
            #텍스트를 분석하고 있습니다.
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            temp_file.write(uploaded_file.read())
            temp_file.close()
            loader = TextLoader(temp_file.name, encoding = 'UTF-8')
            docs = loader.load_and_split(text_splitter=text_splitter)
            #db에 저장하고 있습니다. 시간이 좀 걸릴 수 있습니다.
            db = Chroma.from_documents(
            docs,
            embedding=hf,
            persist_directory= "huggingface5"
                )
            os.remove(temp_file.name) #삭제
            # Process the uploaded file here (e.g., save it, read it, etc.)
            # You can access the file data as uploaded_file.read()
            # Don't forget to close the file after reading it.
            return render_template("main.html", db=db)
    return render_template('upload.html', form=form)