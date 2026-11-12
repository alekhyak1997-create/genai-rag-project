from pathlib import Path
import faiss
import numpy as np

file_path = Path(__file__).parent / "documents" / "knowledge.txt"

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

chunks = [c.strip() for c in text.split("\n\n") if c.strip()]

def embed(text):
    return [
        len(text),
        text.lower().count("python"),
        text.lower().count("ai"),
        text.lower().count("rag")
    ]

vectors = np.array([embed(c) for c in chunks], dtype="float32")

index = faiss.IndexFlatL2(4)
index.add(vectors)

query = "What is RAG?"
query_vector = np.array([embed(query)], dtype="float32")

k = 2

distances, indices = index.search(query_vector, k)

for i in range(k):
    print(f"\nResult {i + 1}:")
    print(chunks[indices[0][i]])
    print("Distance:", distances[0][i])