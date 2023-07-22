from fastapi import APIRouter

produtos = APIRouter()

@produtos.get("/produtos/consultar/{id}")
async def consultar(id):
    return {"message": "Essas produtos estão cadastradas"}

@produtos.post("/produtos/adicionar")
async def adicionar():
    return {"message": "Mais uma produto cadastrado"}

@produtos.patch("/produtos/modificar")
async def modificar():
    return {"message": "Mudou as informações desse produto"}

@produtos.delete("/produtos/remover")
async def remover():
    return {"message": "Esse produto foi removido"}