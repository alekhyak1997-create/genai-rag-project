from pathlib import Path
from sentence_transformers import SentenceTransformer

MODEL_PATH = Path(__file__).parent / "models" / "all-MiniLM-L6-v2"

model = SentenceTransformer(
    str(MODEL_PATH),
    local_files_only=True
)

def embed(text):
    return model.encode(
        text,
        convert_to_numpy=True
    ).astype("float32")