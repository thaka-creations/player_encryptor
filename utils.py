import requests


def list_products():
    url = "http://localhost:8000/api/v1/products"
    try:
        response = requests.get(url)
        return True, response.json()
    except ConnectionError:
        return False, "Connection Error"


def get_file_contents():
    # read file line by line
    with open("file.txt", "r") as f:
        lines = f.readlines()
        return [line.strip() for line in lines]


def write_lines_to_file(lines):
    with open("file.txt", "w"
              ) as f:
        for element in lines:
            f.write(str(element) + '\n')


def write_file(contents):
    with open("file.txt", "w") as f:
        f.write(contents)


def retrieve_product(request_id):
    request_id = request_id.split(" ")[0]
    url = f"http://localhost:8000/api/v1/products/{request_id}"
    try:
        response = requests.get(url)
        return True, response.json()['encryption_key']
    except ConnectionError:
        return False, "Connection Error"
