from pathlib import Path
import faiss
import numpy as np

file_path = Path(__file__).parent / "documents" / "knowledge.txt"

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

vectors = []

for chunk in chunks:
    vector = [
        len(chunk),
        chunk.lower().count("python"),
        chunk.lower().count("ai"),
        chunk.lower().count("rag")
    ]
    vectors.append(vector)

vectors = np.array(vectors, dtype="float32")

index = faiss.IndexFlatL2(4)
index.add(vectors)

print("Chunks stored:", index.ntotal)
print("Vector dimension:", index.d)