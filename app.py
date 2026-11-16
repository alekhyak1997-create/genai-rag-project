import os
import requests
from fastapi import FastAPI, HTTPException, Query
from search import search

app = FastAPI()

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://host.docker.internal:11434"
)
MODEL_NAME = "llama3.2:latest"

@app.get("/")
def home():
    return {"message": "RAG API is running"}


@app.get("/ask")
def ask(question: str = Query(min_length=3, max_length=500)):
    results = search(question)

    if not results:
        raise HTTPException(404, "No relevant documents found")

    prompt = f"""
Answer using only the context.
If the answer is missing, say you don't know.

Context:
{" ".join(results)}

Question: {question}
Answer:
"""

    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )
        response.raise_for_status()
        data = response.json()

    except requests.RequestException as e:
       print("OLLAMA ERROR:", repr(e))
       raise HTTPException(502, "Ollama service is unavailable")

    answer = data.get("response")

    if not answer:
        raise HTTPException(502, "Ollama returned no answer")

    return {
        "question": question,
        "answer": answer.strip(),
        "sources": results
    }

