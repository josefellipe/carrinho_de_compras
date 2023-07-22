from fastapi import APIRouter

pessoas = APIRouter()

@pessoas.get("/pessoas/consultar/{id}")
def consultar(id):
    return {"message": "Essas pessoas estão cadastradas"}

@pessoas.post("/pessoas/adicionar")
def adicionar():
    return {"message": "Mais uma pessoa cadastrada"}

@pessoas.patch("/pessoas/modificar")
def modificar():
    return {"message": "Mudou o cadastro desse cara"}

@pessoas.delete("/pessoas/remover")
def remover():
    return {"message": "Essa pessoa foi removida"}
