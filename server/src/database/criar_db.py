from sqlalchemy import create_engine
from src.database.tables import Base
from sqlalchemy.exc import OperationalError
import os

def criar_db():
    engine = create_engine('sqlite:///pessoa_produto.db', echo=True)
    Base.metadata.create_all(engine)


def verificar_banco_de_dados():
    db_file_path = "pessoa_produto.db"

    if os.path.exists(db_file_path):
        engine = create_engine(f"sqlite:///{db_file_path}")
        try:
            with engine.connect():
                return {'message': 'Banco de dados já existe!'}
        except OperationalError:
            criar_db()
            return {'message': 'Banco de dados criado com sucesso.'}
    else:
        criar_db()
        return {'message': 'Banco de dados criado com sucesso.'}
    