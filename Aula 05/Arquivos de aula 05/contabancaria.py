class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def consultar_saldo(self):
        """Retorna o saldo atual formatado."""
        return f"Saldo atual de {self.titular}: R$ {self.saldo:.2f}"

    def depositar(self, valor):
        """Realiza um depósito na conta."""
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R$ {valor:.2f} realizado com sucesso."
        return "O valor do depósito deve ser maior que zero."

    def sacar(self, valor):
        """Realiza um saque se houver saldo suficiente."""
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R$ {valor:.2f} realizado com sucesso."
        elif valor > self.saldo:
            return "Saldo insuficiente para realizar este saque."
        return "O valor do saque deve ser maior que zero."

minha_conta = ContaBancaria("Amanda", 100.0)

print(minha_conta.consultar_saldo())        
print(minha_conta.depositar(50.0))          
print(minha_conta.sacar(30.0))              
print(minha_conta.consultar_saldo())