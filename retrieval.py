from pathlib import Path
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load the model from your downloaded folder
model_path = Path(__file__).parent.parent / "minilm_model"
model = SentenceTransformer(str(model_path))

# Load document
file_path = Path(__file__).parent / "documents" / "knowledge.txt"

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Split into chunks
chunks = [c.strip() for c in text.split("\n\n") if c.strip()]

# Create semantic embeddings
vectors = model.encode(chunks, convert_to_numpy=True)
vectors = np.array(vectors, dtype="float32")

# Create FAISS index
index = faiss.IndexFlatL2(384)
index.add(vectors)

# Search query
query = "What is RAG?"
query_vector = model.encode([query], convert_to_numpy=True)
query_vector = np.array(query_vector, dtype="float32")

# Retrieve top 2 results
distances, indices = index.search(query_vector, 2)

for i in range(2):
    print(f"\nResult {i + 1}:")
    print(chunks[indices[0][i]])
    print("Distance:", distances[0][i])