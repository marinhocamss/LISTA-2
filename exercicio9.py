class Ponto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Ponto: ({self.x}, {self.y})")


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self):
        x_centro = (self.ponto_inicial.x + self.largura) / 2
        y_centro = (self.ponto_inicial.y + self.altura) / 2
        return Ponto(x_centro, y_centro)


def criarRetangulo():
    x = float(input("Digite uma coordenada x do ponto inferior esquerdo: "))
    y = float(input("Digite uma coordenada y do ponto inferior esquerdo: "))
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))

    ponto_inicial = Ponto(x, y)
    return Retangulo(ponto_inicial, largura, altura)


def main():
    retangulo = None

    while True:
        print('****************Menu: ****************\n')
        print('1. Criar Retângulo \n')
        print('2. Encontrar Centro do Retângulo\n')
        print('3. Sair\n')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            retangulo = criarRetangulo()
        elif opcao == '2':
            if retangulo:
                centro = retangulo.encontrarCentro()
                centro.imprimir()
            else:
                print('Crie um retângulo primeiro.')
        elif opcao == '3':
            break
        else:
            print('Opção inválida. Tente novamente.')


if __name__ == "__main__":
    main()
