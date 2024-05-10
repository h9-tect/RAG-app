from fastapi import FastAPI, Request
from retriever import retrieve_documents
from generator import generate_response

app = FastAPI()

@app.post('/generate')
async def generate_answer(request: Request):
    query = (await request.json())["query"]
    retrieved_docs = retrieve_documents(query)
    response = generate_response(query, retrieved_docs)
    return {"answer": response}
