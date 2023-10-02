class Quadrado:

    def __init__(self, lado):
        self.lado = lado
        
    def mudarValor(self, novo_lado): #mudar o tamanho do lado
        self.lado = novo_lado
    
    def retomarValor(self): #retomar o tamanho do lado
        return self.lado

    def calcularArea(self):
        area = self.lado**2
        return area


#Exemplo
meu_quadrado = Quadrado(8)
print("Tamanho do lado do quadrado: ", meu_quadrado.retomarValor())

meu_quadrado.mudarValor(4)
print("Novo do lado do quadrado: ", meu_quadrado.retomarValor())

print("Área do quadrado: ", meu_quadrado.calcularArea())