# MANIPULAÇÃO DE ARQUIVOS CSV;
# CSV: Comma Separated Values (Valores Separados por Vírgula);

import csv

with open("data/graduacao_unb.csv", encoding="utf-8") as file:
    # os valores padrão de 'delimiter' e 'quotechar' são os mesmos utilizados
    # abaixo. Você pode removê-los ou alterá-los conforme necessidade;

    # delimiter: define que o delimitador dos campos é a vírgula;
    # quotechar: define que as aspas duplas são usadas para citar
    #   campos que contêm delimitadores ou novas linhas;
    graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')

    # usando o conceito de desempacotamento;
    header, *data = graduacao_reader

print(data)

# percorre os dados e agrupa por departamento;
group_by_department = {}

for row in data:
    department = row[15]

    if department not in group_by_department:
        group_by_department[department] = 0
    group_by_department[department] += 1

# escreve o relatório em .csv;
# abre um arquivo para escrita;
with open("department_report.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)

    # escreve o cabeçalho;
    headers = [
        "Departamento",
        "Total de Cursos",
    ]
    writer.writerow(headers)

    # escreve as linhas de dados;
    # desempacotamento de valores;
    for department, grades in group_by_department.items():
        # agrupa o dado com o turno;
        row = [
            department,
            grades,
        ]
        writer.writerow(row)
