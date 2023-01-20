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
from cryptography.fernet import Fernet


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


# check if user is authenticated
def is_authenticated():
    authenticated_user = retrieve_headers()
    if isinstance(authenticated_user, dict):
        return True
    return False


def list_products():
    url = "http://localhost:8000/api/v1/products"
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
    with open("file.txt", "r") as f:
        lines = f.readlines()
        return [line.strip() for line in lines]


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

    with open("properties.json", "w") as f:
        json.dump(file_list, f)


def write_lines_to_file(lines):
    with open("file.txt", "w"
              ) as f:
        for element in lines:
            f.write(str(element) + '\n')

    # get file properties
    write_file_properties(lines)


def write_file(contents):
    with open("file.txt", "w") as f:
        f.write(contents)

    # get file properties
    write_file_properties([contents])


def retrieve_product(request_id):
    request_id = request_id.split(" ")[0]
    url = f"http://localhost:8000/api/v1/products/{request_id}"
    try:
        response = requests.get(url)
        return True, response.json()['encryption_key']
    except ConnectionError:
        return False, "Connection Error"


# send encrypted file to server
def send_encrypted_files(product_id):
    product_id = product_id.split(" ")[0]
    with open("properties.json", "r") as f:
        file_list = json.load(f)

    url = "http://localhost:8000/api/v1/videos/add-video"
    payload = {"product": product_id, "file_list": file_list}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return True, response.json()['message']
    else:
        print(response.json()['message'])
        return False, "Files not sent to server. Try again later"


# check if application is genuine
def is_app_genuine():
    # check if configuration file exists
    if not os.path.exists("config.json"):
        # if user is authenticated, delete credentials
        response = retrieve_headers()
        if isinstance(response, dict):
            keyring.delete_password("tafa_encryptor", "authorization")
            keyring.delete_password("tafa_encryptor", "jwtauth")
        return True
    else:
        # decrypt configuration file
        # key is serial number
        key = base64.urlsafe_b64encode(hashlib.sha256(get_serial_number().encode()).digest()[:32])
        fernet = Fernet(key)

        try:
            with open("config.json", "rb") as file:
                encrypted_data = file.read()
            decrypted_data = fernet.decrypt(encrypted_data)
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
    print("lines", lines)
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
    url = "http://localhost:8000/api/v1/videos/app-registered"
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
            with open("config.json", "wb") as file:
                key = base64.urlsafe_b64encode(hashlib.sha256(get_serial_number().encode()).digest()[:32])
                fernet = Fernet(key)
                encrypted_data = fernet.encrypt(json.dumps(conf).encode())
                file.write(encrypted_data)
            return True
        else:
            if resp != data['app']:
                return False
            else:
                return True

    except Exception as e:
        print(e)
        return False
