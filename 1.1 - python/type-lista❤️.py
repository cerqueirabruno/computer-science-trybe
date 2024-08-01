# LISTA/ARRAY;

# definição: tipo de dado que armazena uma coleção de elementos;
# elementos são definidos separados por vírgula, envolvidos por colchetes;

# declaração de uma lista;
fruits = ["laranja", "maçã", "uva", "abacaxi"]

# declaração de uma lista vazia;
empty_list = []

# acessando elementos de uma lista por índice;
fruits[0]

# acesso por índice negativo (último elemento);
fruits[-1]

# adiciona um elemento ao final da lista;
fruits.append("banana")

# remove um elemento específico da lista;
fruits.remove("banana")

# acrescenta uma lista de frutas a lista original;
fruits.extend(["pera", "melão", "kiwi"])

# retorna o índice de um elemento específico;
fruits.index("maçã")

# ordena a lista de frutas;
fruits.sort()
