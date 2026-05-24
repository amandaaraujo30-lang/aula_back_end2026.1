class Jogo:
    def __init__(self, nome, categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Categoria: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print("-" * 20)