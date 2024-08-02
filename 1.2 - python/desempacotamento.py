# DESENPACOTAMENTO DE VALORES;

# definição: quando queremos separar os valores recebidos em
#   variáveis diferentes;

a, b = "cd"

print(a)  # c
print(b)  # d

head, *tail = (1, 2, 3)

print(head)  # 1
print(tail)  # [2, 3]

# OBS: quando um * está presente no desempacotamento, os valores
# são desempacotados em formato de lista;
