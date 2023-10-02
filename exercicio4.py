class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos =1):
        self.idade += anos
        
        if self.idade < 21: # se for menor de 21 anos a pessoa cresce 0,5m por ano
            self.crescer(anos)

    
    def crescer(self, anos):
        if self.idade < 21:
            self.altura += anos * 0.5


    def engordar(self, kg):
        self.peso += kg

    def emagrecer(self, kg):
        self.peso -= kg

    def __str__(self): #permite imprimir as expressoes da classe
        return f"Nome: {self.nome}\nIdade: {self.idade} anos\nPeso: {self.peso}kg\nAltura: {self.altura}cm "
    
#Exemplo
pessoa1 = Pessoa("Camilla", 19, 58, 1.61)
print(pessoa1)

pessoa1.envelhecer()
print(pessoa1)

pessoa1.engordar(3)
print(pessoa1)

pessoa1.emagrecer(1)
print(pessoa1)