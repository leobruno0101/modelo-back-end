from fastapi import APIRouter, Depends
from models import Usuario
from dependencies import pegar_sessao
from main import decrypt_context

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
    # Session = sessionmaker(bind=db)
    # Session = Session()

    # usuario = Session.query(Usuario).first()

    return{"Mensagem":"Acesso a rota de autenticação"}

@auth_router.post("/criar_conta")
async def criar_conta(nome:str, email:str, senha:str, session = Depends(pegar_sessao)):

    usuario = session.query(Usuario).filter(Usuario.email == email).first()

    if usuario:
        return {"Mensagem" : "Ja existe um usuário com este e-mail"}
    else:
        senha_cripto = decrypt_context.hash(senha)
        novo_usuario = Usuario(nome, email, senha_cripto, usuario)
        session.add(novo_usuario)
        session.commit()
        return {"Mensagem" : "Usuário cadastrado com Sucesso"}