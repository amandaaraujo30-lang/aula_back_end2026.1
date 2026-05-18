# cinema
 
cinema = []
compras = []
preco_ingresso = 20.00
 
def mensagem(msg):
    print(msg)
    input("\nPressione ENTER para continuar...") # Força o terminal a parar para você ler
 
def cadastro_filmes():
    nome_filme = input("Nome do filme: ")
    cinema.append(nome_filme)
    mensagem(f"filme cadastrado! (Valor do ingresso para este filme: R$ {preco_ingresso:.2f})")
 
def mostrar_filmes():
    print("\n==== filmes ====")
    print(f"Preço por ingresso: R$ {preco_ingresso:.2f}")
    print("----------------")
    for i in range(len(cinema)):
        print(f"{i} - {cinema[i]}")
    input("\nPressione ENTER para voltar ao menu...")
 
def compra_filmes(escolha):
    compras.append(cinema[escolha])
    mensagem(f"ingresso comprado com sucesso! Valor: R$ {preco_ingresso:.2f}")
 
def calcular_arrecadacao():
    return len(compras) * preco_ingresso
 
def total_compra():
    return len(compras)
 
def menu():
    print("\n==== cinema DO PYTHON ====")
    print("1 - Cadastrar filmes")
    print("2 - Mostrar filmes")
    print("3 - comprar ingresso")
    print("4 - Total de compras e arrecadação")
    print("5 - Sair")
 
def main():
    while True:
        menu()
        opcao = input("O que deseja fazer?: ").strip()
        
        if opcao == "1":
            cadastro_filmes()
            
        elif opcao == "2":
            if len(cinema) == 0:
                mensagem("Nenhum filme cadastrado ainda! Use a opção 1 primeiro.")
            else:
                mostrar_filmes()
                
        elif opcao == "3":
            if len(cinema) == 0:
                mensagem("Nenhum filme disponível para compra. Cadastre um filme primeiro!")
            else:
                # Mostra os filmes direto sem chamar função para o terminal não se perder
                print("\n==== filmes ====")
                for i in range(len(cinema)):
                    print(f"{i} - {cinema[i]}")
                print(f"Cada ingresso custa R$ {preco_ingresso:.2f}")
                
                escolha_str = input("Escolha o filme pelo número: ").strip()
                if escolha_str.isdigit():
                    num_escolhido = int(escolha_str)
                    if 0 <= num_escolhido < len(cinema):
                        compra_filmes(num_escolhido)
                    else:
                        mensagem("Número de filme inválido!")
                else:
                    mensagem("Por favor, digite um número válido.")
                    
        elif opcao == "4":
            print("\n==== RELATÓRIO DE VENDAS ====")
            print(f"Total de ingressos vendidos: {total_compra()}")
            print(f"Valor unitário do ingresso: R$ {preco_ingresso:.2f}")
            print(f"Total arrecadado: R$ {calcular_arrecadacao():.2f}")
            print("=============================")
            input("\nPressione ENTER para voltar ao menu...")
            
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            mensagem("Opção invalida! Escolha um número de 1 a 5.")
 
main()