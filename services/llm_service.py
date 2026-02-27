import requests
import os
from dotenv import load_dotenv

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_response(prompt, top_chunks=None):
    # Limit prompt size to 20,000 characters
    if len(prompt) > 20000:
        prompt = prompt[:20000]

    # Print prompt length before sending
    print(f"Prompt length: {len(prompt)} characters")

    # Use top 3 relevant retrieved chunks if provided
    if top_chunks:
        relevant_chunks = top_chunks[:3] if len(top_chunks) > 3 else top_chunks
        prompt = prompt.replace("{validated_data}", "\n".join(relevant_chunks))

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5000",   # Required by OpenRouter
        "X-Title": "AgriAgentAI"
    }

    payload = {
        # Use gpt-4o-mini (assuming gpt-4.1-mini is gpt-4o-mini)
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4,
        "max_tokens": 1200
    }

    response = requests.post(url, headers=headers, json=payload)

    # 🔥 Check if request failed
    if response.status_code != 200:
        return f"API Error: {response.text}"

    result = response.json()

    # 🔥 Safe extraction
    if "choices" not in result:
        return f"Unexpected API Response: {result}"

    return result["choices"][0]["message"]["content"]
