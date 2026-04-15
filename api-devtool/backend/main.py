from fastapi import FastAPI
from routes.api_tool import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend is running"}

app.include_router(router, prefix="/api")