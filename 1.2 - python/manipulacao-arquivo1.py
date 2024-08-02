# MANIPULAÇÃO DE ARQUIVOS;

# seja para armazenar alguma informação processada, para manipular imagens,
#   áudios, vídeos ou recuperar dados de uma planilha, precisamos
#   manipular arquivos.


# abre (ou cria, se não existir) um arquivo chamado characters.txt no modo
#   de escrita ("w"). Se o arquivo já existir, seu conteúdo será apagado;
characters_file = open("characters.txt", mode="w")

# escreve no arquivo os nomes dos personagens;
characters_file.write("neo")
characters_file.write("morpheus")
characters_file.write("trinity")

# escreve a string "batman" no arquivo characters.txt usando a função print;
print("batman", file=characters_file)

# criação de uma lista;
more_characters = ["batman", "spiderman", "superman"]

# fecha o arquivo characters.txt;
characters_file.close()
