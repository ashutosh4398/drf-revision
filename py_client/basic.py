import requests

endpoint: str = "http://localhost:8000/api/"

# API Method
# REST API -> WEB Api -> using http request
get_response = requests.post(
    endpoint, json={
        "content": "hello world",
        "title": "hey there",
        "price": "123",
    }, params={"abc": 123}
)
print(get_response.json()) # raw test response

# HTML REQUEST -> HTML
# REST API HTTP REQUEST -> JSON
# print(get_response.json())
print(get_response.status_code)