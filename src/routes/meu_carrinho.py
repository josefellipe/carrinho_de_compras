from fastapi import APIRouter

meu_carrinho = APIRouter()

@meu_carrinho.get("/meu_carrinho/consultar/{id}")
def consultar(id):
    return {"message": "Essas paradas aí que tu tá comprando"}

@meu_carrinho.post("/meu_carrinho/adicionar")
def adicionar():
    return {"message": "Vai levar mais isso"}

@meu_carrinho.patch("/meu_carrinho/modificar")
def modificar():
    return {"message": "Trocou isso por aquilo"}

@meu_carrinho.delete("/meu_carrinho/remover")
def remover():
    return {"message": "Desistiu de comprar isso"}

@meu_carrinho.get("/meu_carrinho/finalizar_compra")
def finalizar_compra():
    return {"message": "Compra finalizada, logo mais chega aí na sua casa! Hehe"}