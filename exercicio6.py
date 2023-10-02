class Tv:

    def __init__(self):
        self.canal_atual = 1 #Está no canal '1'
        self.volume = 10 #Volume varia de 0 a 100, mas no momento está no volume '10'

    def mudar_canal(self, novo_canal):

        if 1 <= novo_canal <= 120: #A Tv vai ter 120 canais
            self.canal_atual = novo_canal
            print("Novo canal: {novo_canal}")

        else:
            print("Canal não encontrado!")       

    def aumentar_volume(self):

        if self.volume < 100:
            self.volume += 1
            print("Volume aumentado para {self.volume}.")

        else:
            print("Volume máximo atingido!")

    def diminuir_volume(self):
        
        if self.volume >= 100:
            self.volume -= 1
            print("Volume diminuido para {self.volume}.")

        else:
            print("Volume já está no mínimo possível!")

    def mostra_estado(self):
        print("Canal atual: {self.canal_atual}")
        print("Volume atual: {self.volume}")

televisor = Tv()

while True: 
    print("*********Opções:*********\n")
    print("Mudar de Canal: '1'\n")
    print("Aumentar o volume: '2'\n")
    print("Diminuir volume: '3'\n")
    print("Mostrar canal e volume: '4'\n")
    print("Sair: '5'\n")

    escolha = int(input("Escolha uma opção: "))

    if escolha == '1':
        novo_canal = int(input("Digite o número do canal: "))
        televisor.mudar_canal(novo_canal)

    elif escolha == '2':
        televisor.aumentar_volume()

    elif escolha == '3':
        televisor.diminuir_volume()

    elif escolha == '4':
        televisor.mostra_estado

    elif escolha == '5':
        print("Saindo.")
        break

    else:
        print("Opção inválida! Tente novamente.")


