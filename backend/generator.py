import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def generate_response(query, retrieved_docs):
    prompt = f"""
    You are a knowledgeable assistant. Use the following documents to answer the question:
    {retrieved_docs}
    The user's question is: {query}
    """
    payload = {
        "model": "llama2",
        "prompt": prompt
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(OLLAMA_API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()["message"]
    else:
        return "Sorry, something went wrong."
