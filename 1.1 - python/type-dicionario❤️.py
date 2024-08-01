# DICIONÁRIO (DICT);

# definição: tipo de dado que armazena pares de chave e valor;

# exemplo 1;
people_by_id = {
    1: "Maria",
    2: "Fernanda",
    3: "Felipe",
}

# exemplo 2;
people_by_name = {
    "Maria": 1,
    "Fernanda": 2,
    "Felipe": 3,
}

# elementos são acessados por suas chaves;
people_by_id[1]

# elementos podem ser removidos com a palavra chave "del";
del people_by_id[1]
