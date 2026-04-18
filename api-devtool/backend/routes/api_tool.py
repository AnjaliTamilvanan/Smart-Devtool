from fastapi import APIRouter
from schemas.api_schema import APIRequest
from services.scraper import scrape_api_docs
from services.ai_parser import parse_api_docs
from services.code_generator import generate_code

router = APIRouter()

@router.post("/analyze-api")
async def analyze_api(data: APIRequest):
    try:
        # Step 1: Scrape API documentation from URL
        raw_text = scrape_api_docs(data.url)

        # Step 2: Parse scraped text using AI
        structured_data = parse_api_docs(raw_text, data.use_case)

        # Step 3: Generate code + sample URL
        generated = generate_code(
            structured_data,
            data.language,
            base_url=data.url  # ✅ FIXED HERE
        )

        return {
            "message": "API analyzed and code generated successfully",
            "structured_data": structured_data,
            "generated_code": generated.get("code", ""),
            "sample_url": generated.get("sample_url", "")
        }

    except Exception as e:
        return {
            "error": str(e),
            "message": "Failed to analyze API"
        }