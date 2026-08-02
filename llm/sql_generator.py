import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_sql(question, schema=None):
    if not question:
        return "SELECT * FROM uploaded_data LIMIT 10;"

    q_lower = question.lower()

    # 1. MINIMUM / LOWEST CAPACITY RULE
    if "minimum" in q_lower or "lowest" in q_lower or "min" in q_lower:
        return "SELECT store_name, city, locality, capacity FROM uploaded_data ORDER BY capacity ASC LIMIT 1;"

    # 2. MAXIMUM / HIGHEST CAPACITY RULE
    if "maximum" in q_lower or "highest" in q_lower or "max" in q_lower:
        return "SELECT store_name, city, locality, capacity FROM uploaded_data ORDER BY capacity DESC LIMIT 1;"

    # 3. COUNT / TOTAL RULE
    if "how many" in q_lower or "count" in q_lower or "total stores" in q_lower:
        return "SELECT COUNT(*) AS total_rows FROM uploaded_data;"

    # 4. CITY LIST RULE
    if "list all cities" in q_lower or "name the cities" in q_lower or "unique cities" in q_lower:
        return "SELECT DISTINCT city FROM uploaded_data ORDER BY city;"

    # Default Fallback
    return "SELECT * FROM uploaded_data LIMIT 10;"