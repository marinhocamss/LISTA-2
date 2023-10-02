class TamagushiMelhorado:

    def __init__(self, nome, fome, saude, idade):
        super().__init__(nome, fome, saude, idade)
        self.comida_fornece = 0
        self.tempo_brinca = 0

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida
        if self.fome < 0:
            self.fome = 0

    def brincar(self, tempo):
        self.tempo_brinca += tempo
        self.fome += tempo * 0.5  # A fome aumenta com o tempo de brincadeira
        if self.fome > 100:
            self.fome = 100

    def mostrar_valores_exatos(self):
        return f"Nome: {self.nome}, Fome: {self.fome}, Saúde: {self.saude}, Idade: {self.idade}, Comida Fornece: {self.comida_fornece}, Tempo de Brincadeira: {self.tempo_brinca}"

    def __str__(self):
        return self.mostrar_valores_exatos()



pou_versao_py = TamagushiMelhorado("Xorumela", 50, 80, 5)
print(pou_versao_py.retornar_informacoes())  # Informações iniciais
print("Humor:", pou_versao_py.calcular_humor())

pou_versao_py.alimentar(30)  # Alimenta com 30 unidades de comida
pou_versao_py.brincar(2)    # Brinca por 2 horas

print(pou_versao_py.retornar_informacoes())  # Informações atualizadas
print("Humor:", pou_versao_py.calcular_humor())

# Mostra os valores exatos dos atributos (opção secreta)
print(pou_versao_py.mostrar_valores_exatos())

print("Valores Exatos:")
print(pou_versao_py)


