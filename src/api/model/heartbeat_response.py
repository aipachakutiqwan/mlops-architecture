"""
Heartbeat pydantic class implementation
"""
from pydantic.main import BaseModel


class HeartbeatResponse(BaseModel):
    """
    Heartbeat pydantic class implementation

    Args:
        :param BaseModel: BaseModel
    """
    is_alive: bool
