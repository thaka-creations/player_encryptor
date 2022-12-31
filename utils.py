import requests


def list_products():
    url = "http://localhost:8000/api/v1/products"
    try:
        response = requests.get(url)
        return True, response.json()
    except ConnectionError:
        return False, "Connection Error"


def get_file_contents():
    with open("file.txt", "r") as f:
        return f.read()


def write_lines_to_file(lines):
    with open("file.txt", "w") as f:
        f.writelines(lines)


def write_file(contents):
    with open("file.txt", "w") as f:
        f.write(contents)
