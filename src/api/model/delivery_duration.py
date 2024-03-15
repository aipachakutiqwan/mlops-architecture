"""
Delivery Duration pydantic class implementation
"""

from pydantic.main import BaseModel
from pydantic.main import List


class DeliveryDuration(BaseModel):
    """
      pydantic class implementation

    Args:
        :param BaseModel: BaseModel
    """
    id: str
    delivery_person_age: float
    delivery_person_ratings: float
    restaurant_latitude: float
    restaurant_longitude: float
    delivery_location_latitude: float
    delivery_location_longitude: float
    weather_conditions: int
    road_traffic_density: int
    vehicle_condition: int
    type_of_order: int
    type_of_vehicle: int
    multiple_deliveries: float
    festival: int
    city: int
    city_code: int
    day: int
    month: int
    quarter: int
    year: int
    day_of_week: int
    is_month_start: int
    is_month_end: int
    is_quarter_start: int
    is_quarter_end: int
    is_year_start: int
    is_year_end: int
    is_weekend: int
    order_prepare_time: float
    distance: int


    def get_id(self) -> str:
        """
        Function to get id .

        Args:
            :param
        Returns:
            id
        """
        id = self.id
        return str(id)