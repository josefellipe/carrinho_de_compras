import os
from dotenv import load_dotenv

load_dotenv()


class User:
    admin_user = os.getenv("ADMIN_USER")
    admin_password = os.getenv("ADMIN_PASSWORD")

