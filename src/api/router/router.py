"""
API routers definition.
"""
from fastapi import APIRouter
from src.api.router import heartbeat, predictions

API_ROUTER = APIRouter()
API_ROUTER.include_router(heartbeat.ROUTER, tags=['Heartbeat'], prefix='/heartbeat')
API_ROUTER.include_router(predictions.ROUTER, tags=['Predictor'], prefix='/predict')
