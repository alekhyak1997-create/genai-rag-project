from pathlib import Path

file_path = Path(__file__).parent / "documents" / "knowledge.txt"

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

print("Number of chunks:",len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}:")
    print(chunk)