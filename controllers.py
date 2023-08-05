from models import Usuario
from views import Views
import hashlib
import re

class Controller:
    @staticmethod
    def criarUsuario(session, nome, email, senha):
        # Checar se a senha é forte
        if not Controller.senhaForte(senha):
            Views.mostrarMensagem("A senha não é forte o suficiente. Ela deve ter pelo menos 8 caracteres, 1 letra maiúscula, 1 letra minúscula e 1 número.")
            return
        # Criptografar a senha que está sendo cadastrada.
        senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()
        novoUsuario = Usuario(nome=nome, email=email, senha=senha_criptografada)
        session.add(novoUsuario) # Adiciona os dados na session
        session.commit()  # Salvar a session no BD.
        Views.mostrarMensagem("Usuário criado com sucesso!")

    @staticmethod
    def fazerlogin(session, email, senha):
        # Criptografar a senha digitada por quem está tentando logar.
        senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()
        # Checar se email e senha existem no BD.
        login = session.query(Usuario).filter_by(email=email, senha=senha_criptografada).first()
        return login

    @staticmethod
    def senhaForte(senha):
        # Verificar se tem no mínimo 8 caracteres.
        if len(senha) < 8:
            return False

        # Verificar se tem letras maiúsculas, minúsculas e números na senha.
        if not (re.search(r'[A-Z]', senha) and
                re.search(r'[a-z]', senha) and
                re.search(r'[0-9]', senha)):
            return False
        # Retorna verdadeiro se as condições acima forem verdadeiras.
        return True
