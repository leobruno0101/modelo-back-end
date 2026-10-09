from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Float, Select
from sqlalchemy.orm import declarative_base

db = create_engine("sqlite:///banco.db")

base = declarative_base()

# Criar as Classes/Tabelas de banco de dados

# Tabela Usuarios
class Usuario(base):
    __tablename__ = "usuarios"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String)
    email = Column('email', String, nullable=False)
    senha = Column('senha', String)
    ativo = Column('ativo', Boolean, default=True)
    admin = Column('admin', Boolean, default=False)

    def __init__(self, nome, email, senha, ativo = True, admin = False):
        self.nome  = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

# Tabela Pedidos
class Pedidos(base):
    __tablename__ = "pedidos"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    status = Column('status', String, nullable=False)
    Usuario = Column('fk_usuario', Integer, ForeignKey("usuarios.id"), nullable=False)
    preco = Column('preco', Float, nullable=False)

    def __init__(self, status, usuario, preco):
        self.status  = status
        self.usuario = usuario
        self.preco   = preco 
                
# Tabela Itens do Pedido

class ItensPedido(base):
    __tablename__ = "itens_pedidos"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    quantidade = Column('quantidade', Integer, default=1)
    sabor = Column('sabor', String, nullable=False)
    tamanho = Column('tamanho', String, nullable=False) 
    preco_unitario = Column('preco_unitario', Float)
    pedido = Column('fk_pedido', Integer, ForeignKey('pedidos.id'), nullable=False)

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido

