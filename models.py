from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

USUARIO = 'root'
SENHA = '219754'
HOST = 'localhost'
BANCO = 'aulapythonfull'
PORT = '3306'

CONN = f'mysql+mysqlconnector://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'

Base = declarative_base()

#Criar tabela no BD.
class Usuario(Base):
    #Nome da tabela.
    __tablename__ = 'Usuários'
    #Colunas da tabela
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    #O tamanho da senha criptografado é  64.
    senha = Column(String(64), nullable=False)