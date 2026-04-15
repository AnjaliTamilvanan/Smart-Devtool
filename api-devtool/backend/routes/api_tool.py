from fastapi import APIRouter
from schemas.api_schema import APIRequest
from services.scraper import scrape_api_docs
from services.ai_parser import parse_api_docs

router = APIRouter()

@router.post("/analyze-api")
async def analyze_api(data: APIRequest):
    # Step 1: Scrape API documentation from URL
    raw_text = scrape_api_docs(data.url)

    # Step 2: Parse scraped text using AI
    structured = parse_api_docs(raw_text, data.use_case)

    # Step 3: Return structured response
    return {
        "message": "API analyzed successfully",
        "structured_data": structured
    }