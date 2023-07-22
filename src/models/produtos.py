from pydantic import BaseModel
from typing import Any

class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    descricao: str
    create_at: Any
    update_at: Any = ''