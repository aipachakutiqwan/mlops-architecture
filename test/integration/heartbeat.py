import os
import sys
import requests
from requests.auth import HTTPBasicAuth
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))


def test_is_alive():
    response = requests.get(
        url="http://localhost:8080/api/heartbeat/heartbeat",
        auth=HTTPBasicAuth('test', 'test')
    )
    print(f'response.status_code: {response.status_code}')
    assert response.status_code == 200


test_is_alive()
