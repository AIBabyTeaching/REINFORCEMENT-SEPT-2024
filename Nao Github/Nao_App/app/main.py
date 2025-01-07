from fastapi import FastAPI  # Corrected import
from app.api.v1.router import api_router

app = FastAPI(title="NAO Backend", version="1.0")

app.include_router(api_router, prefix="/api/v1")
