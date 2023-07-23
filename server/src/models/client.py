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