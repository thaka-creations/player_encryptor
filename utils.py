import requests


def list_products():
    url = "http://localhost:8000/api/v1/products"
    try:
        response = requests.get(url)
        return True, response.json()
    except ConnectionError:
        return False, "Connection Error"
