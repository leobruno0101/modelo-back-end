from fastapi import FastAPI
from auth_routes import auth_router
from order_routes import order_router
from delivery_routes import delivery_router

app = FastAPI()


app.include_router(order_router)

app.include_router(auth_router)

app.include_router(delivery_router)

# uvicorn main:app --reload  - Comando de execução

