documents = [
    "RAG retrieves relevant information from documents.",
    "Python is a programming language.",
    "RAG combines retrieval with an LLM.",
    "Machine learning learns patterns from data."
]

query = "What is RAG?"

relevant = [
    documents[0],
    documents[2]
]

context = "\n".join(relevant)

print("Question:")
print(query)

print("\nContext:")
print(context)