# serve para injecao de dependencias
from fastapi import Depends
from app.db.connection import Session


def get_db_session():
    try:
        session = Session()
        yield session # diferente do retorno ele cai no finally
    finally:
        session.close()
