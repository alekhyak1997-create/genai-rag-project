from pathlib import Path
import numpy as np

file_path = Path(__file__).parent / "documents" / "knowledge.txt"

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

def create_embedding(text):
    vector = np.array([
        len(text),
        text.lower().count("python"),
        text.lower().count("ai"),
        text.lower().count("rag")
    ], dtype="float32")

    return vector

for i, chunk in enumerate(chunks):
    vector = create_embedding(chunk)

    print(f"\nChunk {i + 1}:")
    print(chunk)
    print("Vector:", vector)