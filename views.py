import re

class Views:
    @staticmethod
    def mostrarMensagem(mensagem):
        print(mensagem)

    @staticmethod
    def receberDados(dados):
        return input(dados)

    @staticmethod
    def cadastrar():
        name = Views.receberDados("Digite o name: ")
        email = Views.receberDados("Digite o email: ")
        senha = Views.receberDados("Digite a senha: ")
        return name, email, senha