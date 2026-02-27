import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")


def search_web(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": 5
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    snippets = []

    for result in results.get("organic_results", []):
        snippets.append(result.get("snippet", ""))

    return snippets
