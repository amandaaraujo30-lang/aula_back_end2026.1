# 1. Função para o Menu
def obter_menu():
    return "\n1-Cadastrar | 2-Calcular Desconto | 3-Resumo da Venda | 0-Sair"

# 2. Função para Cadastrar (AJUSTADA PARA ACEITAR VÍRGULA)
def cadastrar_produto():
    nome_produto = input("Nome do produto: ")
    # Lemos como texto, trocamos vírgula por ponto e só aí viramos float
    preco_texto = input("Preço: R$ ")
    preco_produto = float(preco_texto.replace(',', '.')) 
    return nome_produto, preco_produto

# 3. Função para Calcular Desconto
def calcular_desconto(preco):
    return preco * 0.10

# 4. Função para Calcular Total
def calcular_total(preco, valor_desconto):
    return preco - valor_desconto

# --- Execução do Programa ---
nome_item = ""
preco_item = 0.0

while True:
    print(obter_menu())
    opcao = input("Opção desejada: ")

    if opcao == "1":
        nome_item, preco_item = cadastrar_produto()
        print(f"Produto '{nome_item}' cadastrado!")

    elif opcao == "2":
        desconto_valor = calcular_desconto(preco_item)
        print(f"Valor do desconto: R$ {desconto_valor:.2f}")

    elif opcao == "3":
        desconto_valor = calcular_desconto(preco_item)
        total_venda = calcular_total(preco_item, desconto_valor)
        
        print("\n--- RESUMO DA VENDA ---")
        print(f"Produto: {nome_item}")
        print(f"Preço Original: R$ {preco_item:.2f}")
        print(f"Desconto: R$ {desconto_valor:.2f}")
        print(f"Total a Pagar: R$ {total_venda:.2f}")

    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")