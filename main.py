from fastapi import FastAPI
from src.routes.meu_carrinho import meu_carrinho
from src.routes.pessoas import pessoas
from src.routes.produtos import produtos

app = FastAPI()

app.include_router(meu_carrinho)
app.include_router(pessoas)
app.include_router(produtos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)