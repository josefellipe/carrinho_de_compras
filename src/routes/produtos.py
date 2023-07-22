from fastapi import APIRouter

produtos = APIRouter()

@produtos.get("/produtos/consultar/{id}")
def consultar(id):
    return {"message": "Essas produtos estão cadastradas"}

@produtos.post("/produtos/adicionar")
def adicionar():
    return {"message": "Mais uma produto cadastrado"}

@produtos.patch("/produtos/modificar")
def modificar():
    return {"message": "Mudou as informações desse produto"}

@produtos.delete("/produtos/remover")
def remover():
    return {"message": "Esse produto foi removido"}