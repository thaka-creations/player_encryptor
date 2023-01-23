import os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.environ.get("BASE_URL")
TOKEN_KEY = os.environ.get("TOKEN_KEY")
