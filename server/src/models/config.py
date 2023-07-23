import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    admin_user = os.getenv("ADMIN_USER")
    admin_password = os.getenv("ADMIN_PASSWORD")
    host = os.getenv("HOST")
    port=os.getenv("PORT")
    credential=os.getenv("CREDENTIAL")
    db_string=os.getenv("DB_STRING")
