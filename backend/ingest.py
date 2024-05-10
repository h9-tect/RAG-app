import os
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader

# Load and split data
documents = []
loader = TextLoader("data/wiki/sample_data.txt")
splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=0)

for doc in loader.load():
    documents extend(splitter.split_documents([doc]))

# Index data into FAISS
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_db = FAISS.from_documents(documents, embedding)
vector_db.save_local("data/vector_db")

