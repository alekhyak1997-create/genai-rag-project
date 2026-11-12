import requests

url = "http://localhost:11434/api/generate"

try:
    response = requests.post(
        url,
        json={
            "model": "llama3.2",
            "prompt": "Explain RAG in two sentences.",
            "stream": False
        },
        timeout=120
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

except requests.RequestException as error:
    print("Connection error:", error)