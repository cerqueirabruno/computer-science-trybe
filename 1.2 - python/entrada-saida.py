# ENTRADA DE DADOS:

# sys.stdin: entrada padrão do sistema;
import sys


if __name__ == "__main__":
    for argument in sys.argv:
        print("Received -> ", argument)


# input: função que recebe dados do usuário;
user_input = input("Digite uma mensagem: ")

print("O valor recebido foi:", user_input)

# SAIDA DE DADOS:

# print: função que exibe dados na tela;
