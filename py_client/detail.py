import requests
from pprint import pprint
from dataclasses import dataclass

@dataclass
class Auth:
    token: str
    status_code: int

DOMAIN = "http://localhost:8000/api"
class Constants:
    AUTH_URL = f"{DOMAIN}/auth/"
    PRODUCT_LIST_URL = f"{DOMAIN}/products/mixins/"

auth_response = requests.post(Constants.AUTH_URL, json={"username": "staff", "password": "ashutoshthecoder"})

if auth_response.status_code != 200:
    print("AUTHENTICATION FAILED")
    exit()

auth_obj = Auth(status_code=auth_response.status_code, **(auth_response.json()))

authentication_response = auth_response.json()
endpoint: str = ""

# # API Method
# # REST API -> WEB Api -> using http request
get_response = requests.get(
    Constants.PRODUCT_LIST_URL,
    headers={
        "Authorization": f'Bearer {auth_obj.token}'
    }
)
pprint(get_response.json()) # raw test response
