import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_search_queries(profile):
    prompt = f"""
    Generate 3 Google search queries to find government schemes,
    crop insurance, and sustainability benefits for:

    Location: {profile['location']}
    Crop: {profile['crop']}
    Farm Size: {profile['farm_size']}
    Income: {profile['income']}
    """

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-4o-mini",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    data = response.json()
    content = data["choices"][0]["message"]["content"]

    queries = content.split("\n")
    return queries
