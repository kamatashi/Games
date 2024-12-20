import csv



fileTeste = 'deslocamentos.csv'


def square(firstNum, lastNum):
    hourTaked = int(lastNum[0]) - int(firstNum[0])
    minTaked = int(lastNum[1]) - int(firstNum[1])
    return str(hourTaked) + ':' + str(minTaked)


def track(dateTrack):
    time = dateTrack.split(':')
    hour = time[0]
    min = time[1]
    return hour + '.' + min


def takeRow(file, firstCell, lastCell):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            return track(row[firstCell]) - track(row[lastCell])
        



#print(takeRow(fileTeste, 'Saída casa', 'Chegada DIA'))
print(track('45:32:00'))
print(square(['12', '34'],['14', '9']))
