# RANGE;

# definição: função usada para gerar uma sequência de números;
# sintaxe: range( [start], [stop], [step] );

a = list(range(5))

print(a)  # [0, 1, 2, 3, 4]

# list = função que converte o range em uma lista;
# range(5) = gera uma sequência de números de 0 a 4;

# definimos somente o valor de parada
list(range(5))  # saída: [0, 1, 2, 3, 4]

# definimos o valor inicial e o de parada
list(range(1, 6))  # saída: [1, 2, 3, 4, 5]

# definimos valor inicial, de parada e modificamos o passo para 2
list(range(1, 11, 2))  # saída: [1, 3, 5, 7, 9]

# podemos utilizar valores negativos para as entradas também
list(range(10, 0, -1))  # saída: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
