import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    host = os.getenv('HOST')
    port = int(os.getenv('PORT'))
    server_host = os.getenv('SERVER_HOST')
    credential = os.getenv('CREDENTIAL')