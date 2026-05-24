class Animal:
    def __init__(self, nome, tipo, idade):
        self.nome = nome
        self.tipo = tipo
        self.idade = idade
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Tipo: {self.tipo}")
        print(f"Idade: {self.idade} anos\n")