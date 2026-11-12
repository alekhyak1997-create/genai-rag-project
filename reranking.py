documents = [
    "RAG retrieves relevant information from documents.",
    "Python is a programming language.",
    "RAG combines retrieval with an LLM.",
    "Machine learning learns patterns from data."
]

query = "What is RAG?"

results = []

for document in documents:
    score = sum(
        word.lower() in document.lower()
        for word in query.split()
    )
    results.append((score, document))

results.sort(reverse=True)

for score, document in results:
    print("Score:", score)
    print("Document:", document)
    print()