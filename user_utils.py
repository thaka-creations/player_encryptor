import requests
from utils import retrieve_headers
from settings import BASE_URL


def register_user(payload):
    url = f"{BASE_URL}/api/v1/users/register"
    response = requests.post(url, json=payload)
    try:
        if response.status_code == 200:
            return True, response.json()['message']
        else:
            return False, response.json()['message']
    except requests.exceptions.ConnectionError:
        return False, "Could not connect to server. Make sure you are connected to the internet"


def verify_otp(payload):
    url = f"{BASE_URL}/api/v1/users/verify-otp"
    response = requests.post(url, json=payload)
    try:
        if response.status_code == 200:
            return True, response.json()['message']
        else:
            return False, response.json()['message']
    except requests.exceptions.ConnectionError:
        return False, "Could not connect to server. Make sure you are connected to the internet"


def resend_otp(payload):
    url = f"{BASE_URL}/api/v1/users/resend-otp"
    response = requests.post(url, json=payload)
    try:
        if response.status_code == 200:
            return True, response.json()['message']
        else:
            return False, response.json()['message']
    except requests.exceptions.ConnectionError:
        return False, "Could not connect to server. Make sure you are connected to the internet"


def user_details():
    headers = retrieve_headers()
    url = f"{BASE_URL}/api/v1/users/account/user-details"
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return True, response.json()['message']
        elif response.status_code == 403:
            return False, "403"
        else:
            return False, "Page not found"
    except requests.exceptions.ConnectionError:
        return False, "Could not connect to server. Make sure you are connected to the internet"


def logout():
    headers = retrieve_headers()
    url = f"{BASE_URL}/api/v1/users/auth/logout"
    response = requests.post(url, headers=headers)
    try:
        if response.status_code == 200:
            return True, response.json()['message']
        else:
            return True, "Already logged out"
    except requests.exceptions.ConnectionError:
        return False, "Could not connect to server. Make sure you are connected to the internet"





