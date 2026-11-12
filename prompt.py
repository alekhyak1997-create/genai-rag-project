context = """
RAG retrieves relevant information from documents.
RAG combines retrieval with an LLM.
"""

question = "What is RAG?"

prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}

Answer:
"""

print(prompt)