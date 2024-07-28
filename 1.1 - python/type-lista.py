# LISTA/ARRAY;
# definição:  tipo de dado que armazena uma coleção de elementos;
# obs.: não podem ser modificadas durante a execução do programa;
# elementos são definidos separados por vírgula, envolvidos por colchetes;


fruits = ["laranja", "maçã", "uva", "abacaxi"]

fruits[0]  # acesso por índice;

fruits[-1]  # acesso por índice negativo(último elemento);

fruits.append("banana")  # adiciona um elemento ao final da lista;

fruits.remove("abacaxi")  # remove um elemento da lista;

fruits.extend(
    ["pera", "melão", "kiwi"]
)  # acrescenta uma lista de frutas a lista original;

fruits.index("maçã")  # retorna o índice de um elemento específico;

fruits.sort()  # ordena a lista de frutas;
