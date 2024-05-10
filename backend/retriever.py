from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import os

# Load your data and vector database
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_db = FAISS.load_local("./data/vector_db", embedding)

def retrieve_documents(query):
    return vector_db.similarity_search(query)

