import csv

fileTeste = 'deslocamentos.csv'

def takeRow(file):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['Saída casa'], row['Chegada DIA'])


