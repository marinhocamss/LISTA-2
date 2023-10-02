class bombaCombustivel:

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombusivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombusivel
        
    
    def abastecerPorValor(self, valor):
        if valor > 0:
            litro_abastecido = valor/ self.valorLitro

            if litro_abastecido <= self.quantidadeCombustivel:
                self.quantidadeCombustivel -= litro_abastecido
                return(f"Abastecido {litro_abastecido: .2f} litros de {self.tipoCombustivel}.")
            else:
                return print("Quantidade de combustível insuficente na bomba!")
            
        else: 
            return print("Valor de abastecimento inválido!")


    def abastecerPorLitro(self, litro):
        if litro > 0:
            valor_pagar = litro * self.valorLitro

            if litro <= self.quantidadeCombustivel:
                self.quantidadeCombustivel -= litro
                return f"A pagar: R$ {valor_pagar:.2f}."
            else: 
                print("Quantidade de combustível insuficiente na bomba!")

        else:
             return print("Valor de abastecimento inválido!")

        
    def alterarValor(self, novo_valor):
        if novo_valor >= 0:
            self.valorLitro = novo_valor
            return print(f"Valor do litro de {self.tipoCombustivel} alterado para R$ {novo_valor:.2f}.")
        else:
            return print("Valor inválido.")

    def alterarCombustivel(self, novo_combustivel):
        self.tipoCombustivel = novo_combustivel
        return print(f"Tipo de combustível alterado para {novo_combustivel}.")

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        if nova_quantidade >=0:
            self.quantidadeCombustivel = nova_quantidade
            return print(f"Quantidade de combustível alterado para {nova_quantidade}.")
        else:
            return print("Quantidade Inválida!")
        
bomba = bombaCombustivel("Gasolina", 5.0, 1000.0)
print(bomba.abastecerPorValor(50))  # Abastece R$ 50 e retorna a quantidade de litros abastecidos
print(bomba.abastecerPorLitro(20))  # Abastece 20 litros e retorna o valor a ser pago
print(bomba.alterarValor(4.8))       # Altera o valor do litro
print(bomba.alterarCombustivel("Diesel"))  # Altera o tipo de combustível
print(bomba.alterarQuantidadeCombustivel(1500))  # Altera a quantidade de combustível na bomba