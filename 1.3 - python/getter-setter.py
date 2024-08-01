# GETTERS E SETTERS;
# setter implementa a lógica de como alterar um valor;
# getter implementa a lógica de como recuperar um valor;


class Liquidificador:
    def get_cor(self):
        return self.__cor.upper()

    def set_cor(self, nova_cor):
        if nova_cor.lower() == "turquesa":
            raise ValueError("Não existe liquidificador turquesa")

        self.__cor = nova_cor

    def __init__(self, cor, potencia, tensao, preco):
        # observe que usamos o setter para já validarmos o primeiro valor
        self.set_cor(cor)

        # demais variáveis omitidas para este exemplo


liquidificador = Liquidificador("Azul", "110", "127", "200")

print(f"A cor atual é {liquidificador.__cor}")
# AttributeError: 'Liquidificador' object has no attribute '__cor'

print(f"A cor atual é {liquidificador.get_cor()}")
# a cor atual é AZUL

liquidificador.set_cor("Preto")
print(f"Após pintarmos, a nova cor é {liquidificador.get_cor()}")
# após pintarmos, a nova cor é PRETO
