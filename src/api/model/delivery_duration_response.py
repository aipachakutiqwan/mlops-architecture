"""
Delivery Duration response pydantic class implementation
"""

from pydantic.main import BaseModel
from pydantic.main import List


class DeliveryDurationResponse(BaseModel):
    """
    Delivery duration response  pydantic class implementation

    Args:
        :param BaseModel: BaseModel
    """
    
    duration_time: float


PREDICTION_RESPONSES_TYPES = {
    200: {
        "id": "id",
        "label": "label",
        "status": "200"
    },
    400: {"detail": "Expected a valid json message"},
    500: {"detail": "Internal Server Error"},
}
