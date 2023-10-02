class Macaco:

    def __init__(self, nome):
        self.nome = nome
        self.bucho = []
        
    def comer(self, comida):

        self.bucho.append(comida)
        print(f"{self.nome} comeu {comida}.")
    
    def verBucho(self):
        print(f"O {self.nome} tem no bucho: {', '.join(self.bucho)}.")

    def digerir(self):

        if self.bucho:
            print(f"{self.nome} está digerindo {self.bucho[0]}.")

        else:
            print(f"O {self.nome} não tem nada no bucho?")


macaco1 = Macaco('Xorumela')
macaco2 = Macaco('Risadinha')

macaco1.comer('cenoura')
macaco1.comer('uva')
macaco2.comer('bolo de cenoura')

macaco1.verBucho()
macaco2.verBucho()

macaco1.digerir()
macaco1.verBucho()

macaco1.comer("banana")
macaco2.comer("abacaxi")
macaco2.comer("chocolate")

macaco1.digerir()
macaco2.digerir()

macaco1.verBucho()
macaco2.verBucho()

