# MANIPULAÇÃO DE ARQUIVOS JSON;

import json  # json é um modulo que vem embutido, porém precisamos importá-lo;

with open("data/pokemons.json") as file:
    pokemons = json.load(file)["results"]

print(pokemons[0])  # imprime o primeiro pokemon da lista;
print(pokemons)  # imprime todos os pokemons da lista;


# separamos somente os do tipo grama;
grass_type_pokemons = []

for pokemon in pokemons:
    if "Grass" in pokemon["type"]:
        grass_type_pokemons.append(pokemon)

# imprime todos os pokemons do tipo grama;
print(grass_type_pokemons)


# abre o arquivo para escrevermos apenas o pokemons do tipo grama;
with open("grass_pokemons.json", "w") as file:
    # conversão de python para o formato json (str);
    json_to_write = json.dumps(grass_type_pokemons)
    file.write(json_to_write)


# OBERVAÇÕES;
# desserialização: transformação de texto em formato JSON para Python;
# serialização: transformação de Python para texto em formato JSON;

# leitura de todos os pokemons
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

# Separamos somente os do tipo grama
grass_type_pokemons = []
for pokemon in pokemons:
    if "Grass" in pokemon["type"]:
        grass_type_pokemons.append(pokemon)

# abre o arquivo para escrita
with open("grass_pokemons.json", "w") as file:
    # escreve no arquivo já transformando em formato json a estrutura
    json.dump(grass_type_pokemons, file)
