import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY") or st.secrets.get("OPENROUTER_API_KEY")

MODEL = "deepseek/deepseek-chat-v3-0324:free"

def generate_sql(question, schema):

    prompt = f"""
You are an expert SQLite SQL generator.

Table name: uploaded_data

Columns:
{schema}

Rules:
- Return ONLY SQL.
- SQLite syntax only.
- No markdown.

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

    st.write(result)   # <-- IMPORTANT

    if "choices" not in result:
        st.error(result)
        return "SELECT * FROM uploaded_data LIMIT 5;"

    return result["choices"][0]["message"]["content"].strip()