from fastapi import APIRouter
from schemas.api_schema import APIRequest
from services.scraper import scrape_api_docs

router = APIRouter()

@router.post("/analyze-api")
async def analyze_api(data: APIRequest):
    # Step 1: Scrape API documentation from URL
    raw_text = scrape_api_docs(data.url)

    # Step 2: Return response with preview
    return {
        "message": "Scraping successful",
        "preview": raw_text[:300]
    }