#. Definição dos dados (Uso de listas/dicionarios)
jogos = ["Minecraft", "GTA V", "FIFA"]
precos = [80, 120, 90]
carrinho = []
total = 0
print("--- BEM-VINDO A LOJA DE GAMES---")

#2 Mostrar os jogos disponiveis
print("\nJogos disponiveis:")
for i in range(len(jogos)):
    print(f"{i} - {jogos[i]}): R${precos[i]}")

#3 Permitir compra (Laço de repetição)
while True:
    escolha = input("\nDigite o numero do jogo para comprar (ou 'sair' para finalizar): ")
    if escolha.lower() == 'sair':
        break

    #Verificar se a entrada é um número valido
    if escolha.isdigit():
        indice = int(escolha)
    if 0 <= indice < len(jogos):

        carrinho.append(precos[indice])
        print(f"{jogos[indice]}adicionado ao carrinho!")
    else:
        print("Entrada invalida! Digite o numero do jogo.")
    
#4 Somar valores
total = sum(carrinho)

#5 Verificar desconto (condicional)
#Regra: se a compra  passar de R$200 -> desconto de 10%
desconto = 0
if total > 200:
    desconto = total * 0.10

total_com_desconto = total - desconto

#6 Mostra o resultado final
print("\n" + "="*30)
print(" Resumo da Compra")
print("="*30)
print(f"Total da compra: R${total:.2f}")

if desconto > 0:
    print(f"Desconto (10%): R${desconto:.2f}")
    print(f"Total a pagar: R${desconto:.2f}")
else:
    print("Sem desconto aplicado (compras abaixo de R$200).")
    print(f"Total a pagar: R${total:.2f}")
    print("="*30)