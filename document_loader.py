from pathlib import Path
file_path = Path(__file__).parent / "documents" / "knowledge.txt"
with open(file_path, "r",encoding="utf-8") as file:
    text = file.read()

print("Document:")
print(text)

print("\nCharacters:", len(text))