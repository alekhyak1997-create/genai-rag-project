from pathlib import Path
import faiss

from embedding import embed

# Get the project folder
base = Path(__file__).parent

# Load document
text = (base / "documents" / "knowledge.txt").read_text(
    encoding="utf-8"
)

# Split document into chunks
chunks = [c.strip() for c in text.split("\n\n") if c.strip()]

# Load FAISS index
index_path = base / "rag.index"

if not index_path.exists():
    raise FileNotFoundError(
        "rag.index not found. Run build_index.py first."
    )

index = faiss.read_index(str(index_path))

# Search function
def search(query, top_k=1):

    # Convert query into semantic embedding
    vector = embed(query).reshape(1, -1)

    # Check vector dimensions
    if vector.shape[1] != index.d:
        raise ValueError("Embedding and FAISS dimensions do not match.")

    # Normalize query vector
    faiss.normalize_L2(vector)

    # Search FAISS index
    scores, ids = index.search(vector, top_k)

    # Collect matching chunks
    results = []

    for score, i in zip(scores[0], ids[0]):
        if i != -1:
            results.append(chunks[i])

    return results


# Run directly for testing
if __name__ == "__main__":

    query = "What is RAG?"

    results = search(query)

    print("\nQuestion:", query)
    print("\nRetrieved results:")

    if results:
        for result in results:
            print("-", result)
    else:
        print("No relevant information found.")