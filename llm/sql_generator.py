import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Get API Key from Streamlit Secrets (for Cloud) or Environment (for Local)
API_KEY = st.secrets.get("OPENROUTER_API_KEY") or os.getenv("OPENROUTER_API_KEY")

# Reliable Free Model Slug on OpenRouter for SQL Generation
MODEL = "google/gemma-2-9b-it:free"

def generate_sql(question, schema):
    if not API_KEY:
        st.error("⚠️ OpenRouter API Key is missing! Please set OPENROUTER_API_KEY in Streamlit Secrets.")
        return ""

    prompt = f"""
You are an expert SQLite SQL generator.

Table name: uploaded_data

Columns:
{schema}

Rules:
- Return ONLY SQL.
- No markdown formatting (do not use ```sql or ```).
- No explanation or conversational text.
- Valid SQLite syntax only.
- Use uploaded_data table.

Question:
{question}
"""

    try:
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

        # Check for error in response
        if "error" in result:
            st.error(f"API Error: {result['error'].get('message', result['error'])}")
            return ""

        if "choices" in result and len(result["choices"]) > 0:
            sql_clean = result["choices"][0]["message"]["content"].strip()
            # Remove any accidental markdown backticks if returned
            sql_clean = sql_clean.replace("```sql", "").replace("```", "").strip()
            return sql_clean
        else:
            st.error(f"Unexpected response format from API: {result}")
            return ""

    except Exception as e:
        st.error(f"Connection Error: {e}")
        return ""