import csv
import requests

data = requests.get('https://raw.githubusercontent.com/PatrickFenger/pythonAssignments/master/KoreanConflict.csv')

def get_data():
    with open('korean_conflict.csv', 'w') as f:
        writer = csv.writer(f)
        reader = csv.reader(data.text.splitlines())

        for row in reader:
            writer.writerow(row)


    