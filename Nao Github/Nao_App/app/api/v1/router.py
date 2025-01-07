# router.py placeholder file
from fastapi import APIRouter
from app.api.v1.endpoints import ml_models, nao_controller, health_check

api_router = APIRouter()
api_router.include_router(ml_models.router, prefix="/ml", tags=["Machine Learning"])
api_router.include_router(nao_controller.router, prefix="/nao", tags=["NAO"])  # Fixed typo
api_router.include_router(health_check.router, prefix="/health", tags=["Health"])
