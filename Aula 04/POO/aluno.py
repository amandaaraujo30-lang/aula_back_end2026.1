class Aluno:

    #Metodo comnstrutor (todo que tiver se criado automaticamente quando a classe for usada)
    #O metodo __init__ é um metodo padrão
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


aluno_um = Aluno("Marcos", 25)
print(f"Nome: {aluno_um.nome}")
print(f"Idade: {aluno_um.idade}")

print(20*"-"\n)
      
aluno_dois = Aluno("Maria",30)
print(f"Nome: {aluno_dois.nome}")
print(f"Idade: {aluno_dois.idade}")

print(20*"-"\n)

nome= input ("Informe o nome do primeiro aluno: ")
idade = int(input("informe a idade: "))
aluno_tres = Aluno(nome,idade)
print(aluno_tres.nome)
print(aluno_tres.idade)
