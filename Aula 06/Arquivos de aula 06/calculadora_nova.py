class Calculadora:
    def __init__(self, numero_um, numero_dois):
        """Inicializa os atributos da classe."""
        self.numero1 = numero_um
        self.numero2 = numero_dois

    def somar(self):
        return self.numero1 + self.numero2

    def subtrair(self):
        return self.numero1 - self.numero2

    def multiplicar(self):
        return self.numero1 * self.numero2

    def dividir(self):
        # Tratamento simples para evitar divisão por zero
        if self.numero2 == 0:
            return "Erro: Divisão por zero não permitida."
        return self.numero1 / self.numero2

# --- Testando o Sistema ---

# 1. Criando o objeto (instanciando a classe)
minha_calc = Calculadora(10, 5)

# 2. Executando os métodos e exibindo os resultados
print(f"Número 1: {minha_calc.numero1} | Número 2: {minha_calc.numero2}")
print("-" * 30)
print(f"Soma:          {minha_calc.somar()}")
print(f"Subtração:     {minha_calc.subtrair()}")
print(f"Multiplicação: {minha_calc.multiplicar()}")
print(f"Divisão:       {minha_calc.dividir()}")