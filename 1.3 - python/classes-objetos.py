# CONSTRUCTOR:
# definição:
# self: é uma referência ao próprio objeto.


# exemplo 1:
class Exemplo:
    def __init__(self):
        print("Inicializando Exemplo")

    def __new__(cls, *args, **kwargs):
        print("Criando uma nova instância de Exemplo")
        instance = super().__new__(cls)
        return instance


# exemplo 2:
class Liquidificador:
    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.cor = cor
        self.potencia = potencia
        self.tensao = tensao
        self.ligado = False
        self.velocidade = 0
        self.velocidade_maxima = 3
        self.corrente_atual_no_motor = 0


# exemplo de criação:
meu_liquidificador = Liquidificador("Azul", 200, 127, 200)

seu_liquidificador = Liquidificador(cor="Vermelho", potencia=250, tensao=220, preco=100)
