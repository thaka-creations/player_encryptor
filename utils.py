import json
import os
import requests
import ffmpeg
import keyring
import base64
import hashlib
import platform
import subprocess
import plistlib

from PyQt5.QtCore import QSettings

from settings import BASE_URL, TOKEN_KEY
from cryptography.fernet import Fernet

ss = QSettings("TafaEncryptor", "TafaEncryptor")


# store headers using keyring
def store_headers(authorization, jwtauth, refresh_token):
    try:
        keyring.set_password("tafa_encryptor", "authorization", f"Bearer {authorization}")
        keyring.set_password("tafa_encryptor", "jwtauth", f"Bearer {jwtauth}")
        keyring.set_password("tafa_encryptor", "refresh_token", f"Bearer {refresh_token}")
        return True
    except Exception as e:
        print(e)
        return False


# retrieve headers from keyring
def retrieve_headers():
    try:
        authorization = keyring.get_password("tafa_encryptor", "authorization")
        jwt = keyring.get_password("tafa_encryptor", "jwtauth")
        if authorization is None or jwt is None:
            return False
        return {"Authorization": authorization, "JWTAUTH": jwt}
    except Exception as e:
        print(e)
        return False


# delete headers
def delete_headers():
    if keyring.get_password("tafa_encryptor", "authorization"):
        keyring.delete_password("tafa_encryptor", "authorization")
        keyring.delete_password("tafa_encryptor", "jwtauth")
        keyring.delete_password("tafa_encryptor", "refresh_token")


# check if user is authenticated
def is_authenticated():
    authenticated_user = retrieve_headers()
    if isinstance(authenticated_user, dict):
        # check if headers are valid
        url = f"{BASE_URL}/api/v1/users/account/user-details"
        response = requests.get(url, headers=authenticated_user)
        if response.status_code == 200:
            return True
        else:
            return False
    return False


def list_products():
    url = f"{BASE_URL}/api/v1/products"
    headers = retrieve_headers()
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return True, response.json()
        elif response.status_code == 403:
            return False, "Unauthorized"
        else:
            return False, "Something went wrong"
    except ConnectionError:
        return False, "Connection Error"


def get_file_contents():
    # read file line by line
    file_contents = ss.value("file_contents")
    return file_contents


def write_file_properties(contents):
    # get file properties
    file_list = []

    for element in contents:
        name = os.path.basename(element)
        size = os.stat(element).st_size
        extension = os.path.splitext(element)[1]

        try:
            info = ffmpeg.probe(element)
            duration = float(info['format']['duration'])
        except Exception as e:
            print(e)
            duration = None

        file_list.append({
            "name": name,
            "size": size,
            "extension": extension,
            "duration": duration,
            "file_path": element
        })

    ss.setValue("file_properties", file_list)
    # read file
    print("file_list writing", ss.value("file_properties"))


def write_lines_to_file(lines):
    write_file(lines)


def write_file(contents):
    ss.setValue("file_contents", contents)

    # get file properties
    write_file_properties(contents)


def retrieve_product(request_id):
    request_id = request_id.split(" ")[0]
    url = f"{BASE_URL}/api/v1/products/{request_id}"
    try:
        response = requests.get(url)
        return True, response.json()['encryption_key']
    except ConnectionError:
        return False, "Connection Error"


# add product to server
def add_product(payload):
    headers = retrieve_headers()
    url = f"{BASE_URL}/api/v1/products"
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return True, response.json()
        elif response.status_code == 403:
            return False, "403"
        else:
            return False, response.json()
    except ConnectionError:
        return False, "Connection Error"


# send encrypted file to server
def send_encrypted_files(product_id):
    product_id = product_id.split(" ")[0]
    file_list = ss.value("file_properties")
    print("file_list", file_list)

    url = f"{BASE_URL}/api/v1/videos/add-video"
    payload = {"product": product_id, "file_list": file_list}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return True, response.json()['message']
    else:
        return False, "Files not sent to server. Try again later"


# check if application is genuine
def is_app_genuine():
    # check if configuration file exists
    if not keyring.get_password("tafa_encryptor", "config"):
        # if user is authenticated, delete credentials
        response = retrieve_headers()
        if isinstance(response, dict):
            keyring.delete_password("tafa_encryptor", "authorization")
            keyring.delete_password("tafa_encryptor", "jwtauth")
        return True
    else:
        # decrypt configuration file
        # key is serial number
        token = TOKEN_KEY
        key = base64.urlsafe_b64encode(hashlib.sha256(token.encode()).digest()[:32])
        fernet = Fernet(key)

        try:
            encrypted_data = keyring.get_password("tafa_encryptor", "config")
            # with open("config.json", "rb") as file:
            #     encrypted_data = file.read()
            decrypted_data = fernet.decrypt(encrypted_data.encode())
            return json.loads(decrypted_data)
        except Exception as e:
            print(e)
            return False


# mac serial number
def get_mac_serial_number():
    # Run the system_profiler command and retrieve the output
    output = subprocess.check_output(['system_profiler', 'SPHardwareDataType'])
    # Convert the output to a string and split it into lines
    lines = output.decode().split('\n')
    # Iterate over the lines and find the line containing the serial number
    for line in lines:
        if 'Serial Number' in line:
            # Split the line into words and return the second word (the serial number)
            return line.split()[-1]


# windows serial number
def get_windows_serial_number():
    output = subprocess.run(["wmic", "bios", "get", "serialnumber"], stdout=subprocess.PIPE).stdout.decode("utf-8")
    serial_number = output.split("\n")[1]
    return serial_number


# get computer's os
def get_serial_number():
    os_type = platform.system()
    if "darwin" in os_type.lower():
        serial_number = get_mac_serial_number()
        print("mac serial number", serial_number)
    else:
        serial_number = get_windows_serial_number()
        print("windows serial number", serial_number)
    return serial_number


def get_mac_model_name():
    pl = subprocess.run(["system_profiler", "SPHardwareDataType", "-xml"], capture_output=True).stdout
    plist = plistlib.loads(pl)
    model_name = plist[0]['_items'][0]['machine_model']
    return model_name


def get_windows_model_name():
    output = subprocess.run("wmic csproduct get name", shell=True, capture_output=True, text=True)
    model_name = output.stdout.strip().split("\n")[1]
    return model_name


def get_model_mame():
    os_type = platform.system()
    if "darwin" in os_type.lower():
        model_name = get_mac_model_name()
    else:
        model_name = get_windows_model_name()
    return model_name


def app_registered():
    url = f"{BASE_URL}/api/v1/videos/app-registered"
    payload = {"serial_number": get_serial_number(), "model_name": get_model_mame(), "encryptor": True}
    response = requests.post(url, json=payload)

    if not response.status_code == 200:
        return False
    try:
        resp = response.json()['message']

        # check if conf file exists
        data = is_app_genuine()
        if isinstance(data, bool):
            if not data:
                return False

            # write file
            conf = {"app": resp}
            token = TOKEN_KEY
            key = base64.urlsafe_b64encode(hashlib.sha256(token.encode()).digest()[:32])
            fernet = Fernet(key)
            encrypted_data = fernet.encrypt(json.dumps(conf).encode())
            keyring.set_password("tafa_encryptor", "config", encrypted_data.decode())
            return True
        else:
            if resp != data['app']:
                return False
            else:
                return True

    except Exception as e:
        print(e)
        return False
