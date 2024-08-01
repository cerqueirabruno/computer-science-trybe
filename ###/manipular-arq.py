# MANIPULAÇÃO DE ARQUIVOS;
open("arquivo.txt", "r")  # abre o arquivo em modo de leitura
open("arquivo.txt", "w")  # abre o arquivo em modo de escrita

file = open("arquivo.txt", mode="w")
# ao abrir um arquivo para escrita, um novo arquivo é criado mesmo que ele
# já exista, sobrescrevendo o antigo;


file.close()  # fecha o arquivo;

# OBS: witch.open("arquivo.txt", mode="r") as file:  # abre o arquivo e o
# fecha automaticamente ao final do bloco;

# print("Túlio 22", file=file) # escreve no arquivo;

# writelines: escreve uma lista de strings no arquivo;
#    LINES = ["Alberto 35\n", "Betina 22\n", "João 42\n", "Victor 19\n"]
#    file.writelines(LINES)

# RESUMOS:
# escrita
with open("arquivo.txt", "w") as file:
    file.write("Trybe S2")

# leitura
with open("arquivo.txt", "r") as file:
    content = file.read()
    print(content)
