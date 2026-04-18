import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# ✅ Clean LLM JSON output
def clean_json_output(text):
    cleaned = text.replace("```json", "").replace("```", "").strip()
    try:
        return json.loads(cleaned)
    except:
        return {}


# ✅ Validate endpoints (only real ones)
def filter_valid_endpoints(endpoints):
    valid = []

    for ep in endpoints:
        url = ep.get("url", "").strip()

        if url.startswith("/") or url.startswith("http"):
            valid.append(ep)

    return valid


# 🚀 MAIN FUNCTION
def parse_api_docs(text, use_case):
    prompt = f"""
Analyze this API documentation and extract structured data.

Return STRICT JSON with:

- endpoints: list of objects [
    {{
      "url": "ONLY real API endpoint (must start with / or http)",
      "method": "GET/POST/etc",
      "description": "short clear description"
    }}
  ]

- parameters: list of objects [
    {{
      "name": "...",
      "in": "query/path/header",
      "required": true/false,
      "description": "..."
    }}
  ]

- authentication: string
- sdk_suggestion: string

STRICT RULES:
- ONLY extract real API endpoints
- URL must contain "/" or "http"
- DO NOT return titles like "Weather API"
- If unsure, skip endpoint
- Output ONLY JSON

Use case: {use_case}

{text}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a strict API parser. Output ONLY valid JSON."
                },
                {"role": "user", "content": prompt}
            ]
        )

        result = response.choices[0].message.content
        parsed = clean_json_output(result)

    except Exception as e:
        print("AI parsing error:", e)
        parsed = {}

    # ✅ Ensure structure safety
    if not isinstance(parsed, dict):
        parsed = {}

    endpoints = parsed.get("endpoints", [])
    parsed["endpoints"] = filter_valid_endpoints(endpoints)

    parsed.setdefault("parameters", [])
    parsed.setdefault("authentication", "")
    parsed.setdefault("sdk_suggestion", "")

    # ✅ Attach use case
    parsed["use_case"] = use_case

    return parsed