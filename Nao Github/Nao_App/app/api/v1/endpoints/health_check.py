# health_check.py placeholder file
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_check():
    return {"status": "Healthy"}
