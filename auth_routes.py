from fastapi import APIRouter
from models import Usuario, db
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix="/autenticador", tags=["Autenficação"])

@auth_router.get("/")

async def autenticar():
    """
        Você esta na rota de Autentificação
        siga as instruções a segui para criar um novo Usuário: <br>
        1 - Nome<br>
        2 - Senha<br>
        3 - Letras maiusculas e minusculas
    """
    Session = sessionmaker(bind=db)
    Session = Session()

    usuario = Session.query(Usuario).first()

    return{"Mensagem":f"Usuários = {usuario}"}

@auth_router.post("/criar_conta")
async def criar_conta(nome:str, email:str, senha:str):
    Session = sessionmaker(bind=db)
    Session = Session()

    usuario = Session.query(Usuario).filter(Usuario.email == email).first()

    if usuario:
        return {"Mensagem" : "Ja existe um usuário com este e-mail"}
    else:
        novo_usuario = Usuario(nome, email, usuario)
        Session.add(novo_usuario)
        Session.commit()
        return {"Mensagem" : "Usuário cadastrado com Sucesso"}