"""Função com passagem de parametros"""
def ola_aluno(nome):
    print(f"Ola {nome}!")


nome_usuario = input("insira seu nome: ")
nome_usuario_2 = input("insira seu nome: ")

ola_aluno(nome_usuario)
ola_aluno(nome_usuario_2)