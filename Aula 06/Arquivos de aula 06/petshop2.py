class Animal:
 
    def __init__(self, nome, tipo, idade):
        self.nome = nome
        self.tipo = tipo
        self.idade = idade
   
    def desc_animal(self):
         print(f'O animal {self.nome},\ntipo é {self.tipo}, \na idade é {self.idade}')
 
#----------------------------------------------------------------------
 
class PetShop:
 
    def __init__(self):
        self.cadastro = [] #lista
       
    def cadastrar_animal(self):
        nome = input('Nome do animal: ')
        tipo = input('Tipo: ')
        idade = int(input('Idade: '))
 
        animal = Animal(nome, tipo, idade) #a variavel animal se torna um Objeto
 
        self.cadastro.append(animal)
 
        print('cadastro feito')
   
    def mostrar_animais(self):
        print('\n Animais Cadastrados')
 
        for animal in self.cadastro:
            animal.desc_animal()
 
    """      cadastro = [
            #dicionario ou objeto
            {
                'nome': "Chcuc",
                'tipo': 'Gato',
                'idade': '2'
             }
 
        ] """
 
 
pet = PetShop()
pet.cadastrar_animal()
pet.mostrar_animais()