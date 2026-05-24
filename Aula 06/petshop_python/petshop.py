#Ligação com o arquivo animal.py e com classe Animal
#animal minusculo é o nome do arquivo
#Animal com a primeira letra em maiusculo é o nome da classe
#from nome_arquivo import nome_classe
from animal import Animal

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
                                
#execução
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