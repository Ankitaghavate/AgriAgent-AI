from agents.sustainability_agent import calculate_score
from agents.reasoning_agent import generate_structured_report
from services.rag_service import RAGService
import requests
import os

# Initialize RAG service
rag = RAGService()
rag.load_index()  # Make sure faiss_index.pkl exists


def process_farmer(user_input):
    # 1️⃣ Farmer profile
    profile_data = user_input

    # 2️⃣ Retrieve relevant scheme info from RAG
    query = f"Based on this farmer profile: {profile_data}"
    retrieved_chunks = rag.retrieve(query, top_k=3)
    validated_data = "\n".join(retrieved_chunks)

    # 3️⃣ Optional: fallback to SERP if RAG finds nothing
    if not validated_data.strip():
        validated_data = "Fallback: Search results from web (SERP API can go here)."

    # 4️⃣ Calculate sustainability score
    sustainability_score = calculate_score(profile_data)

    # 5️⃣ Generate final structured report
    final_report = generate_structured_report(
        profile_data,
        validated_data,
        sustainability_score
    )

    return final_report
