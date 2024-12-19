import csv


with open('deslocamentos.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Saída casa'], row['Chegada DIA'])
