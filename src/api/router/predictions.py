"""
Implementation predict route
"""
from fastapi import APIRouter
from starlette.requests import Request
from src.handlers.predictor import Predictor
from src.api.model.delivery_duration_response import PREDICTION_RESPONSES_TYPES
from src.api.model.delivery_duration import DeliveryDuration
from src.api.model.delivery_duration_response import DeliveryDurationResponse


ROUTER = APIRouter()

@ROUTER.post("/delivery/duration", response_model=DeliveryDurationResponse, responses=PREDICTION_RESPONSES_TYPES)
async def forecating_delivery_duration(delivery_duration: DeliveryDuration, request: Request):
    """
    Notifies about the arrival new request for predict delivery duration

    Args:
        :param  delivery_duration: delivery_duration
        :param  request: request

    Returns:
        FastAPI endpoint configured
    """
    handler: Predictor = request.app.state.predictor
    delivery_duration_response = handler.predict_delivery_duration(delivery_duration)
    return delivery_duration_response
