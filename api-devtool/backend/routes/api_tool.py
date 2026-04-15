from fastapi import APIRouter
from schemas.api_schema import APIRequest

router = APIRouter()

@router.post("/analyze-api")
async def analyze_api(data: APIRequest):
    return {
        "message": "API received successfully",
        "data": data
    }