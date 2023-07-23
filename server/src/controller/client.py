from fastapi import APIRouter, Request

from src.models.client import ClientRegister
from src.models.config import Config



client = APIRouter()

@client.get("/client/consult/{id}")
async def consult(id):
    return {"message": "Essas client estão cadastradas"}

@client.post("/client/create")
async def create_client(informations: ClientRegister, request: Request):
    credential = request.headers.get("credential")
    if credential != Config.credential:
        return {
            "success": False,
            "message": "Você não pode ter acesso a essa API"
        }
    


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

    return response

@client.patch("/client/modify")
async def modify():
    return {"message": "Mudou o cadastro desse cara"}

@client.delete("/client/delete")
async def delete():
    return {"message": "Essa pessoa foi removida"}
