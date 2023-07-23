from fastapi import FastAPI
import uvicorn

from models.config import Config

from view.login.app import login

app = FastAPI()

app.include_router(login)



if __name__ == "__main__":
    uvicorn.run(
        app,
        host=Config.host, 
        port=Config.port
    )