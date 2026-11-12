context = """
RAG retrieves relevant information from documents.
RAG combines retrieval with an LLM.
"""

question = "What is RAG?"

prompt = f"""
Answer using only the context.

Context:
{context}

Question:
{question}
"""

print("Prompt:")
print(prompt)

answer = "RAG retrieves relevant information from documents and uses an LLM to generate an answer."

print("\nAnswer:")
print(answer)