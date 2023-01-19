import requests


def register_user(payload):
    url = "http://localhost:8000/api/v1/users/register"
    response = requests.post(url, json=payload)
    try:
        if response.status_code == 200:
            return True, response.json()['message']
        else:
            return False, response.json()['message']
    except requests.exceptions.ConnectionError:
        return False, "Could not connect to server. Make sure you are connected to the internet"


def verify_otp(payload):
    url = "http://localhost:8000/api/v1/users/verify-otp"
    response = requests.post(url, json=payload)
    try:
        if response.status_code == 200:
            return True, response.json()['message']
        else:
            return False, response.json()['message']
    except requests.exceptions.ConnectionError:
        return False, "Could not connect to server. Make sure you are connected to the internet"


def resend_otp(payload):
    url = "http://localhost:8000/api/v1/users/resend-otp"
    response = requests.post(url, json=payload)
    try:
        if response.status_code == 200:
            return True, response.json()['message']
        else:
            return False, response.json()['message']
    except requests.exceptions.ConnectionError:
        return False, "Could not connect to server. Make sure you are connected to the internet"
