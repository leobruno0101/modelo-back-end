from fastapi import APIRouter

delivery_router = APIRouter(prefix="/entrega", tags=["entrega"])

@delivery_router.get("/entrega")

async def entrega():
    """
        Para entregar basta pedir
    """
    return{"Mensagem": "A entrega foi feita"}