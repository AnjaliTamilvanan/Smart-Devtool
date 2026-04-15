from pydantic import BaseModel

class APIRequest(BaseModel):
    url: str
    use_case: str
    language: str