class Tamagushi: #Criando um Pou

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = 0       #'0' significa que o Pou 2.0 não está com fome
        self.saude = 100    # '100' significa que o Pou 2.0 não está doente, está 100% bem
        self.idade = 0
    
    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, valor):

        if 0 <= valor <= 100:
            self.fome = valor

        else: 
            print("Valor escolhido para a fome do seu tamagushi inválido! Tente novamente!")

    def alterarSaude(self,valor):

        if 0 <= valor <= 100:
            self.saude = valor
        else: 
            print("Valor escolhido para a saúde do seu tamagushi inválido! Tente novamente!")

    def alterarIdade(self, anos):

        if anos >= 0:
             self.idade += anos
        
        else:
            print("Valor escolhido para a idade do seu tamagushi inválido! Tente novamente!")

    def retomarNome(self):
        return self.nome

    def retomarFome(self):
        return self.fome

    def retomarSaude(self):
        return self.saude

    def retomarIdade(self):
        return self.idade

    def humor(self):
        return (self.fome + self.saude)//2
    

        
pou_versão_py = Tamagushi('Xorumela', 28, 80, 4)

pou_versão_py.alterarIdade(5)
pou_versão_py.alterarSaude(16)
pou_versão_py.alterarFome(55)

print(f"Nome: {pou_versão_py.retomarNome()} ")
print(f"Idade: {pou_versão_py.retomarIdade()} ")
print(f"Fome: {pou_versão_py.retomarFome()} ")
print(f"Saúde: {pou_versão_py.retomarSaude()} ")
print(f"Humor: {pou_versão_py.humor()} ")
