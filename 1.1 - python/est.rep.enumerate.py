# ENUMERATE;
# definição: retorna um objeto enumerate, que é uma sequência de tuplas
# contendo o índice e o valor de cada item em uma lista;


languages = ["Python", "Java", "JavaScript"]

enumerate_prime = enumerate(languages)

print(list(enumerate_prime))  # [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]
