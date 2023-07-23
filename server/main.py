from fastapi import FastAPI
import uvicorn

from src.models.config import Config

from src.database.criar_db import verify_db
from src.controller.meu_carrinho import meu_carrinho
from src.controller.client import client
from src.controller.produtos import produtos

verify_db()

app = FastAPI()

app.include_router(meu_carrinho)
app.include_router(client)
app.include_router(produtos)


if __name__ == "__main__":
    uvicorn.run(
        app,
        #host=Config.host,
        #port=Config.port
        host="localhost", 
        port=8080
    )