from pydantic import BaseModel
from typing import Any


class Carrinho(BaseModel):
    id: int
    id_pessoa: int
    id_produto: int
    qtd: int
    status: int
    create_at: Any
    update_at: Any = ''

