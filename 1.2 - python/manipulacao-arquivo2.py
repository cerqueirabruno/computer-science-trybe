# GERENCIADOR DE CONTEXTO (with);

# o gerenciador de contexto é uma forma de garantir que os
#   recursos sejam liberados após a execução de um bloco
#   de código, mesmo que ocorra uma exceção.

# sintaxe de escrita;
with open("arquivo.txt", "w") as file:
    # escrevendo uma linha
    file.write("Miguel 33\n")

    # não precisa da quebra de linha, pois esse é um
    #   comportamento padrão do print
    print("Túlio 22", file=file)

    # escrevendo multiplas linhas
    LINES = ["Alberto 35\n", "Betina 22\n", "João 42\n", "Victor 19\n"]
    file.writelines(LINES)

# sintaxe de leitura;
with open("arquivo.txt", "r") as file:
    content = file.read()
    print(content)


# iterando sobre as linhas;
# escrita
with open("arquivo.txt", "w") as file:
    LINES = ["Olá\n", "mundo\n", "belo\n", "do\n", "Python\n"]
    file.writelines(LINES)

# leitura
with open("arquivo.txt", "r") as file:
    for line in file:
        # não esqueça que a quebra de linha também é um caractere da linha
        print(line)
