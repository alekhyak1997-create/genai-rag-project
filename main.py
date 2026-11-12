
from pathlib import Path
import ollama
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
# Load the semantic embedding model
model_path = Path(__file__).parent.parent / "minilm_model"

model = SentenceTransformer(str(model_path))

print("Embedding model loaded successfully")
# 1. Load document
file_path = Path(__file__).parent / "documents" / "knowledge.txt"

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# 2. Split document into chunks
chunks = [c.strip() for c in text.split("\n\n") if c.strip()]

# 3. User question
query = "What is RAG?"

# 4. Retrieve relevant chunks
results = [
    chunk for chunk in chunks
    if "rag" in chunk.lower()
]

# 5. Build context
context = "\n".join(results)

# 6. Generate answer using Ollama
response = ollama.chat(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": f"""
    you are a helpful AI Assistant        
Answer using only the context below.
Include all relevant information from the context.
Do not give an answer shorter than necessary.
Do not use information outside the context.

Context:
{context}

Question:
{query}
"""
        }
    ]
)

answer = response["message"]["content"]

# 7. Display results
print("Question:", query)
print("\nRetrieved Context:")
print(context)
print("\nAnswer:")
print(answer)
