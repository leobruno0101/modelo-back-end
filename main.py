from fastapi import FastAPI

from passlib.context import CryptContext
from dotenv import load_dotenv

import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

decrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from auth_routes import auth_router
from order_routes import order_router
from delivery_routes import delivery_router

app.include_router(order_router)

app.include_router(auth_router)

app.include_router(delivery_router)

# uvicorn main:app --reload  - Comando de execução

