from fastapi import APIRouter

pessoas = APIRouter()

@pessoas.get("/pessoas/consultar/{id}")
async def consultar(id):
    return {"message": "Essas pessoas estão cadastradas"}

@pessoas.post("/pessoas/adicionar")
async def adicionar():
    return {"message": "Mais uma pessoa cadastrada"}

@pessoas.patch("/pessoas/modificar")
async def modificar():
    return {"message": "Mudou o cadastro desse cara"}

@pessoas.delete("/pessoas/remover")
async def remover():
    return {"message": "Essa pessoa foi removida"}
