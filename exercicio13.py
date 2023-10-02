class Funcionário:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def ter_nome(self):
        return self.nome

    def ter_salario(self):
        return self.salario
    

funcionário1 = Funcionário("Camilla Marinho", 1580.0) #bem pobrinha

funcionário1.ter_nome()
funcionário1.ter_salario()
print(f"Nome do Funcionário: ", funcionário1.ter_nome())
print(f"Salário: ", funcionário1.ter_salario())

