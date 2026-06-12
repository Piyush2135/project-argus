import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:7b"

SYSTEM_PROMPT = """
You are an expert quiz solving AI.

The input comes from OCR and may contain noise.
Ignore unrelated text, UI labels, timestamps, and OCR errors.
Identify the actual question and options.
Infer the correct answer.

Rules:
- Reply with ONLY the correct option or answer.
- If options are present, output the full option text.
- Do NOT explain.
- Do NOT add extra sentences.
"""

def ask_ollama(question):
    payload = {
        "model": MODEL,
        "prompt": f"System:\n{SYSTEM_PROMPT}\n\nUser:\n{question}",
        "stream": False,
        "options": {
            "temperature": 0,
            "top_k": 10,
            "top_p": 0.8,
            "num_predict": 15,
            "num_ctx": 2048
        }
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=30
    )

    response.raise_for_status()

    return response.json()["response"].strip()