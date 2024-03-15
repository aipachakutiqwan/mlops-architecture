import sys
import os
import requests
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))


def test_api_delivery_duration(id):

    payload = {"id": id, 
               "delivery_person_age":30.0,
               "delivery_person_ratings":5.0,
               "restaurant_latitude":22.744648,
               "restaurant_longitude":75.894377,
               "delivery_location_latitude":22.824648,
               "delivery_location_longitude":75.974377,
               "weather_conditions":1,
               "road_traffic_density":3,
               "vehicle_condition":0,
               "type_of_order":3,
               "type_of_vehicle":2,
               "multiple_deliveries":0.0,
               "festival":1,
               "city":0,
               "city_code":10,
               "day":20,
               "month":3,
               "quarter":1,
               "year":2022,
               "day_of_week":6,
               "is_month_start":0,
               "is_month_end":0,
               "is_quarter_start":0,
               "is_quarter_end":0,
               "is_year_start":0,
               "is_year_end":0,
               "is_weekend":1,
               "order_prepare_time":15.0,
               "distance":12
               }

    response = requests.post(
        url="http://localhost:8080/api/predict/delivery/duration",
        json=payload,
        proxies={"https": "", "http": ""}

    )
    print(f'Response delivery duration service : {response.text}')
    print(f'Status code delivery duration service : {response.status_code}')
    assert response.status_code == 200

id = "12345"
test_api_delivery_duration(id)