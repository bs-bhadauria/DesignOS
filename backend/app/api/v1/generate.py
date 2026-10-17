from fastapi import APIRouter, Depends, Form, File, UploadFile
from typing import List, Optional

from app.core.dependencies import get_generation_service
from app.schemas.generate import GenerateResponse
from app.services.generation_service import GenerationService

router = APIRouter(
    prefix="/api/v1",
    tags=["Generation"],
)


@router.get("/health")
async def health_check():
    return {"status": "ok", "message": "Backend is running!"}


@router.post(
    "/generate",
    response_model=GenerateResponse,
)
async def generate_document(
    prompt: str = Form(...),
    files: Optional[List[UploadFile]] = File(None),
    generation_service: GenerationService = Depends(
        get_generation_service
    ),
):

    return await generation_service.generate(
        prompt=prompt,
        files=files
    )