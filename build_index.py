from pathlib import Path
import faiss
import numpy as np
from embedding import embed

# Project folder
base = Path(__file__).parent

# Read knowledge document
text = (base / "documents" / "knowledge.txt").read_text(
    encoding="utf-8"
)

# Split document into chunks
chunks = [c.strip() for c in text.split("\n\n") if c.strip()]

# Convert chunks into semantic embeddings
vectors = np.array(
    [embed(chunk) for chunk in chunks],
    dtype="float32"
)

# Normalize vectors
faiss.normalize_L2(vectors)

# Create FAISS index
index = faiss.IndexFlatIP(vectors.shape[1])

# Add vectors to index
index.add(vectors)

# Save FAISS index
faiss.write_index(index, str(base / "rag.index"))

# Display results
print("Chunks:", len(chunks))
print("Vector dimension:", vectors.shape[1])
print("Index rebuilt successfully.")
