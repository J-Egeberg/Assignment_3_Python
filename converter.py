import requests
from contextlib import closing
import csv

url = "http://download-and-process-csv-efficiently/python.csv"

with closing(requests.get(url, stream=True)) as r:
    reader = csv.reader(r.iter_lines(), delimiter=',', quotechar='"')
    for row in reader:
        print row 