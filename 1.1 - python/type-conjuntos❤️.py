# CONJUNTOS (SET);

# únicos e não ordenados;
# elementos separados por vírgula, envol vidos por chaves;
# implementam operações de união, intersecção e outras;

# sintaxe;
permissions = {
    "member",
    "group",
}

# adicionar um novo elemento ao conjunto;
permissions.add("root")

# como o elemento já existe, nenhum novo item é adicionado ao conjunto;
permissions.add("member")

# retorna um conjunto resultado da união;
permissions.union({"user"})

# retorna um conjunto resultante da intersecção dos conjuntos;
permissions.intersection({"user", "member"})

# retorna a diferença entre os dois conjuntos;
permissions.difference({"user"})
