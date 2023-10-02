class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    

    def mostrarCor(self):
        return self.cor
    
    def trocarCor(self, nova_cor):
        self.cor = nova_cor
        

#Exemplo
minha_bola = Bola("verde", 25, "borracha")
print("Cor da bola: ", minha_bola.mostrarCor()) #imprimi a cor da bola

minha_bola.trocarCor("vermelho")
print("Nova cor da bola: ", minha_bola.mostrarCor()) #imprimir nova cor da bola