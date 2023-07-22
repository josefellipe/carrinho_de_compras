from fastapi import APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os


view = APIRouter()


dirname = os.path.dirname(__file__)
view.mount("/static", StaticFiles(directory=os.path.join(dirname, 'static')), name="static")

templates = Jinja2Templates(directory=os.path.join(dirname, 'templates'))


# Rota para a página inicial ("/")
@view.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("readme.html", {"request": request})


# Rota para a página "/home"
@view.get("/home", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
