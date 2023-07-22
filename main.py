from fastapi import FastAPI
import uvicorn

from src.database.criar_db import verificar_banco_de_dados
from src.controller.meu_carrinho import meu_carrinho
from src.controller.pessoas import pessoas
from src.controller.produtos import produtos

from src.view.views import view

verificar_banco_de_dados()

app = FastAPI()

app.include_router(meu_carrinho)
app.include_router(pessoas)
app.include_router(produtos)

app.include_router(view)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0", 
        port=8000
    )