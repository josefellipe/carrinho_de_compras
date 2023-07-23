from fastapi import APIRouter, Request
from src.models.client import ClientRegister

client = APIRouter()

@client.get("/client/consult/{id}")
async def consult(id):
    return {"message": "Essas client estão cadastradas"}

@client.post("/client/create")
async def create_client(informations: ClientRegister, request: Request):
    credential = request.headers.get("credential")
    
    if informations.name == 'A':
        response = {
            "success": True,
            "message": "Conta criada com sucesso!"
        }
    else:
        response = {
            "success": False,
            "message": "Não foi possível criar a conta."
        }


    print(informations, credential)
    return response

@client.patch("/client/modify")
async def modify():
    return {"message": "Mudou o cadastro desse cara"}

@client.delete("/client/delete")
async def delete():
    return {"message": "Essa pessoa foi removida"}
