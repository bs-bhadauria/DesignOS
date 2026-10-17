from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/")
def health_check():
    return {
        "success": True,
        "message": "DesignOS Backend is running 🚀",
        "version": "0.1.0"
    }
