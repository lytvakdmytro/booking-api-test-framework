import os

BASE_URL = os.getenv("BASE_URL", "https://restful-booker.herokuapp.com")
TIMEOUT = float(os.getenv("TIMEOUT", "10"))
