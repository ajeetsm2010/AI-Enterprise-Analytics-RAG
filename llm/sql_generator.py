import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "deepseek/deepseek-chat-v3-0324:free"

def generate_sql(question, schema):

    prompt = f"""
You are an expert SQLite SQL generator.

Table name: uploaded_data

Columns:
{schema}

Rules:
- Return ONLY SQL.
- No markdown.
- No explanation.
- SQLite syntax only.
- Use uploaded_data table.

Question:
{question}
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },
        timeout=60
    )

    result = response.json()

    return result["choices"][0]["message"]["content"].strip()