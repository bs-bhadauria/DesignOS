from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.v1.generate import router as generate_router

api_router = APIRouter()

api_router.include_router(health_router)

api_router.include_router(generate_router)
