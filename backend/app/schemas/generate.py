from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    prompt: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="User prompt",
    )


class GenerateResponse(BaseModel):
    success: bool
    request_id: str
    status: str
    html: str