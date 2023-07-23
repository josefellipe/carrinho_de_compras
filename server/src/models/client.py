from pydantic import BaseModel
from typing import Any


class Client(BaseModel):
    id: int
    name: str
    email: str
    password: str
    create_at: Any
    update_at: Any = ''




class ClientRegister(BaseModel):
    name: str
    email: str
    password: str

    def __init__(self, name: str, email: str, password: str):
        super().__init__(name=name, email=email, password=password)

        engine = ''

    def change_email(self, new_email: str):
        self.email = new_email