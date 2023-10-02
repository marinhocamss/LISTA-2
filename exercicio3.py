class Retangulo:

    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
        
    def mudarLado(self, novo_comprimento, nova_largura):
        self.comprimento = novo_comprimento
        self.largura = nova_largura
    
    def retomarLado(self):
        self.comprimento
        self.largura

    def calcularArea(self):
        area = self.comprimento * self.largura
        return area

    def calcularPerimetro(self):
       perimetro = (self.comprimento * 2) + (self.largura*2)
       return perimetro
    

meu_retangulo = Retangulo(10, 4)
print("Lados", meu_retangulo.retomarLado())
print("Perimetro do Retangulo: ", meu_retangulo.calcularPerimetro())
print("Área do Retangulo: ", meu_retangulo.calcularArea())

meu_retangulo.mudarLado(8,3)
print("Novos lados: ", meu_retangulo.retomarLado())
print("Npvo perimetro do Retangulo: ", meu_retangulo.calcularPerimetro())
print("Nova área do Retangulo: ", meu_retangulo.calcularArea())

