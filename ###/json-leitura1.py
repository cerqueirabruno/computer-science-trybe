import json

with open("data.json") as data_file:
    data_content = json.load(data_file)  # exite load, loads e dump, dumps

print(data_content)  # acessando o conteudo do arquivo

print(data_content[1])  # acessando um elemento

for name in data_content:
    print(name["name"])
