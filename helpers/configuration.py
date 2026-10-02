import os

from dotenv import load_dotenv

load_dotenv()


class Configuration:
    base_url = os.getenv("BASE_URL", "https://restful-booker.herokuapp.com")
    auth_username = os.getenv("AUTH_USERNAME", "admin")
    auth_password = os.getenv("AUTH_PASSWORD", "password123")
