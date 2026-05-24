class Calculadora:
    def __init__(self, n1, n2):
        """Construtor para inicializar os atributos da classe."""
        self.numero1 = n1
        self.numero2 = n2

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

# --- Testando a Classe ---

# 1. Instanciando o objeto com dois valores
meu_calculo = Calculadora(10, 5)

# 2. Executando os métodos e exibindo os resultados
print(f"Calculadora POO - Valores: {meu_calculo.numero1} e {meu_calculo.numero2}")
print("-" * 30)
print(f"Soma:          {meu_calculo.somar()}")
print(f"Subtração:     {meu_calculo.subtrair()}")
print(f"Multiplicação: {meu_calculo.multiplicar()}")
print(f"Divisão:       {meu_calculo.dividir()}")