from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str

class GenerateResponse(BaseModel):
    result: str