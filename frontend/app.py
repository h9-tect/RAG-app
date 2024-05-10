import streamlit as st
import requests

st.title("RAG Chatbot")
query = st.text_input("Ask your question:")

if st.button("Submit"):
    response = requests.post(
        'http://backend:8000/generate',
        json={"query": query}
    ).json()
    st.write(response["answer"])

