from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@order_router.get("/lista") # @ Decorator

async def pedidos():
    """
        Você está na rota de pedidos <br>
        Faça seu pedido e informe: <br>
        1 - ID <br>
        2 - Quantidade
    """

    return{"Mensagem":"Eu vou dormir bem hoje"}

