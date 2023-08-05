from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Usuario, CONN
from controllers import Controller
from views import Views


def main():
    engine = create_engine(CONN)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        Views.mostrarMensagem("\n1 - Criar Usuário\n2 - Fazer Login\n0 - Sair")
        escolha = Views.receberDados("Escolha uma opção: ")

        if escolha == "1": #Cadastrar usuário
            nome, email, senha = Views.cadastrar()
            emailCadastrado = session.query(Usuario).filter_by(email=email).first()
            if emailCadastrado: #Checa se o email já está cadastrado no BD
                Views.mostrarMensagem("Já existe um usuário com esse email.")
            #TODO fazer verificação de senha forte.
            else: #se não, cadastra o usuário no banco de dados
                Controller.criarUsuario(session, nome, email, senha)

        elif escolha == "2": #Fazer login
            email = Views.receberDados("Email: ")
            senha = Views.receberDados("Senha: ")
            login = Controller.fazerlogin(session, email, senha)
            #Manda o email e senha pra controller checar se eles existem no BD
            if login:
                Views.mostrarMensagem("Login efetuado com sucesso.")
            else:
                Views.mostrarMensagem("Email ou senha invalida.")

        elif escolha == "0": #Voltar ao menu
            break

        else: #Mensagem de erro
            Views.mostrarMensagem("Opção invalida, tente novamente")

if __name__ == "__main__":
    main()
