from pydantic import BaseModel, Field


class ValidateRequest(BaseModel):
    word: str = Field(..., min_length=1)
