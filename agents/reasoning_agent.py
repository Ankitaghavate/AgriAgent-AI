from services.llm_service import generate_response


def generate_structured_report(profile_data, validated_data, sustainability_score, top_chunks=None):

    prompt = f"""
You are an expert agricultural policy advisor.

Generate a professional advisory report.

FORMAT STRICTLY:

Executive Summary

Eligible Government Schemes

Subsidies

Insurance & Vima Schemes

Loan & Financial Assistance

Sustainability Recommendations

Green Skill Programs

Final Advisory Score

Farmer Profile:
{profile_data}

Validated Government Data:
{validated_data}

Sustainability Score:
{sustainability_score}

IMPORTANT:
Do NOT use markdown symbols like *, -, #.
Write in clean professional paragraphs.
"""

    return generate_response(prompt, top_chunks=top_chunks)
