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
        return lines


def write_lines_to_file(lines):
    print("lines", lines)
    with open("file.txt", "w"
              ) as f:
        for element in lines:
            f.write(str(element) + '\n')


def write_file(contents):
    with open("file.txt", "w") as f:
        f.write(contents)
