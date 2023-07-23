from fastapi import APIRouter, Request, Form
from fastapi import exceptions
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models.config import Config

import os
import requests


login = APIRouter()
host_port = f'{Config.host}:{Config.port}'

dirname = os.path.dirname(__file__)

templates = Jinja2Templates(directory=os.path.join(dirname, 'templates'))

# Rota para a página inicial ("/")
@login.get("/cadastre_se", response_class=HTMLResponse)
async def read_root(request: Request):
    context = {"request": request, "host": host_port}
    return templates.TemplateResponse("cadastre_se.html", context=context)


# Rota para a página "/home"
@login.get("/login", response_class=HTMLResponse)
async def render_login(request: Request):
    context = {"request": request, "host": host_port}
    return templates.TemplateResponse("login.html", context=context)


@login.post("/cadastre_se", response_class=HTMLResponse)
async def cadastro_submit(request: Request, name: str = Form(...), email: str = Form(...), password: str = Form(...), confirmPassword: str = Form(...)):
    if password != confirmPassword:
        context = {
            "request": request,
            "error": "Senhas diferentes",
            "host": host_port
        }
        return templates.TemplateResponse("cadastro_sucesso.html", context=context)
    
    url = f"{Config.server_host}/client/create"
    json = {
        'name': name,
        'email': email,
        'password': password
    }

    headers = {
        'Content-Type': 'application/json',
        'credential': Config.credential
    }

    try:
        response = requests.post(url=url, headers=headers, json=json)
        response.raise_for_status()  # Lança uma exceção para códigos de status HTTP >= 400
        data = response.json()
        message = data["message"]
        success = data["success"]
    except requests.exceptions.RequestException as e:
        message = "Erro ao tentar acessar o servidor, tente novamente mais tarde!"
        success = False

    context = {
        "success": success,
        "request": request,
        "message": message,
        "host": host_port
    }

    print(context)
    print(response)

    return templates.TemplateResponse("cadastre_se.html", context=context)

    
    
