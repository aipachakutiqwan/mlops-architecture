"""
Heartbeat router implementation
"""
from fastapi import APIRouter
from src.api.model.heartbeat_response import HeartbeatResponse

ROUTER = APIRouter()


@ROUTER.get("/heartbeat", response_model=HeartbeatResponse, name="heartbeat")
def get_heartbeat() -> HeartbeatResponse:
    """
    Heartbeat API router implementation

    Returns:
        HeartbeatResult: pydantic heartbeat class
    """
    heartbeat = HeartbeatResponse(is_alive=True)
    return heartbeat
