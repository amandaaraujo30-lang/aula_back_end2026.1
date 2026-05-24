class Animal:
    def __init__(self, nome, tipo, idade):
        self.nome = nome
        self.tipo = tipo
        self.idade = idade
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Tipo: {self.tipo}")
        print(f"Idade: {self.idade} anos\n")

class PetShop:
    def __init__(self):
        #lista de animais do petshope
        self.lista_animais = []

    def cadastrar_animal(self):
        print("--- Cadastro de Animal ---")
        nome = input("Nome: ")
        tipo = input("Tipo: ")
        idade = input("Idade: ")

        #Criando o objeto animal e adicionando a lista
        novo_animal = Animal(nome, tipo, idade)
        self.lista_animais.append(novo_animal)
        print("Animal cadastrado com sucesso!\n")

    def mostrar_animais(self):
        if not self.lista_animais:
            print("nenhum animal cadastrado no sistema.")
        else:
            print("--- Lista de Animais---")
            for animal in self.lista_animais:
                animal.mostrar_dados()
                
#execulção
def executar_sistema():
    meu_pet_shop = PetShop()
    while True:
        print("1. Cadastrar Animal")
        print("2. Mostrar Animais")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao =="1":
            meu_pet_shop.cadastrar_animal()
        elif opcao =="2":
            meu_pet_shop.mostrar_animais()
        elif opcao == "3":
            break
        else:
            print("Opção invalida!\n")
if __name__ == "__main__":
    executar_sistema()