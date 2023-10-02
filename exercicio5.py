class ContaCorrente: 

    def __init__(self, numero_conta, nome, saldo = 0.0):
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, valor):

        if valor > 0:
            self.saldo += valor
            return True
        
        else:
            return False
        

    def saque(self, valor):

        if valor > 0 and self.saldo > valor:
            self.saldo-= valor
            return True
        else:
            return False
          
    def __str__(self):

        return f"Conta {self.numero_conta}: {self.nome}, Saldo: R${self.saldo:.2f}"


conta1 = ContaCorrente(1075, "Camilla Marinho", 700)
print(conta1)

#Fazendo um saque

if conta1.saque(100):
    print("Saque de R$ 100,00 realizado com sucessso!")

else:
    print("Não foi possível realizar saque. Saldo insuficiente!!")

if conta1.deposito(96):
    print("Depósito de R$96,00 realizado com sucesso!")

else:
    ("Erro ao realizar o depósito!")
