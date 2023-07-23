from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.tables import Base
from sqlalchemy.exc import OperationalError

from src.models.config import Config
import os

def create_db():
    engine = create_engine(Config.db_string, echo=True)
    Base.metadata.create_all(engine)


def verify_db():
    db_file_path = "store.db"

    if os.path.exists(db_file_path):
        engine = create_engine(f"sqlite:///{db_file_path}")
        try:
            with engine.connect():
                return {'message': 'Banco de dados já existe!'}
        except OperationalError:
            create_db()
            return {'message': 'Banco de dados criado com sucesso.'}
    else:
        create_db()
        return {'message': 'Banco de dados criado com sucesso.'}
    

def create_session():
    try:
        engine = create_engine(Config.db_string, echo=True)
        Session = sessionmaker(bind=engine)
        return Session()
    except Exception as e:
        return None