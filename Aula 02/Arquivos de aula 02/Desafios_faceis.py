#idade 
def mostrar_idade(ano_nascimento):
    idade = 2026 - ano_nascimento
    print (f"Você tem {idade}")

mostrar_idade (1993)

#idade2
def mostrar_idade(ano_nascimento):
    idade = 2026 - ano_nascimento
    print (f"Você tem {idade}")

ano_nascimento = int(input("Informe o ano em que você nasceu: "))
mostrar_idade (ano_nascimento)


#cidade
def mostrar_cidade(nome_cidade):
    print(f"Você moda em: {nome_cidade}")
    
mostrar_cidade("Rio de Janeiro")

#produto
def mostrar_produto(nome):
    print(f"Produto: {nome}")

    mostrar_produto("celular")
    mostrar_produto("caderno")
