from pydantic import BaseModel
from typing import Any



class Pessoa(BaseModel):
    id: int
    nome: str
    email: str
    senha: str
    create_at: Any
    update_at: Any = ''

