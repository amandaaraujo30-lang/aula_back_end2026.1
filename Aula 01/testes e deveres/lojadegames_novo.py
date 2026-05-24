class Jogo:
    def __init__(self, nome, categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome} | Categoria: {self.categoria} | Preço: R$ {self.preco:.2f}")

class Loja:
    def __init__(self):
        # Composição: a lojapassui uma lista de objetos do tipo de jogo
        self.lista_jogos = []
    
    def cadastrar_jogo(self):
        print("\n--- Cadastrode Jogo ---")
        nome = input("Digite o nome do jogo: ")
        categoria = input("Digite a categoria: ")
        preco = float(input("Digite o preço:"))

        #Criando o objeto Jogo e armazenando na lista
        novo_jogo = Jogo(nome, categoria, preco)
        self.lista_jogos.append(novo_jogo)
        print(f"Jogo '{nome}'cadastrado com sucesso!")

    def mostrar_jogos(self):
        print("\n--- Lista de Jogos Cadastrados ---")
        if not self.lista_jogos:
            print("Nenhum jogo cadastrado no momento.")
        else:
            for jogo in self. lista_jogos:
                jogo.mostrar_dados()

    def iniciar(self):
        #Controle do menu totalmente interno à classe Loja
        while True:
            print("\n==== MENU DA LOJA DE GAMES ====")
            print("1.Cadastrar Jogo")
            print("2. Mostrar Jogos")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")
        
            if opcao == "1":
                self.cadastrar_jogo()
            elif opcao == "2":
                self.mostrar_jogos()
            elif opcao == "3":
                print("Encerrando o sistema... Até logo!")
                break
            else:
                print("Opcão inválida! Tente novamente.")

# --- Execulção do Sistema ---
# Tudo acontece através da instancia do objeto 'minha_loja'
minha_loja = Loja()
minha_loja.iniciar()