import requests

endpoint: str = "http://localhost:8000/api/products/1/update/"

# API Method
# REST API -> WEB Api -> using http request
get_response = requests.put(
    endpoint,
    json={
        "title": "Amkette",
        "price": "12"
    }
)
print(get_response.json()) # raw test response

# HTML REQUEST -> HTML
# REST API HTTP REQUEST -> JSON
# print(get_response.json())
print(get_response.status_code)