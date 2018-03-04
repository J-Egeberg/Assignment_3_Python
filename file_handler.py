import csv
import requests
import os.path
import shutil

def download_file(file_name, url):
    split = url.split("/")
    og_file_name = split[len(split) - 1]
    print("Downloaded " + file_name)
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(og_file_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
            os.rename("./" + og_file_name, "./" + file_name)


def get_csv_sheet():
    csv_sheet_name = "korean_conflict.csv"
    if not os.path.exists("./" + csv_sheet_name):
        download_file(csv_sheet_name, 'https://raw.githubusercontent.com/PatrickFenger/pythonAssignments/master'
                                      '/KoreanConflict.csv')
    csvfile = open(csv_sheet_name)
    return csv.reader(csvfile, delimiter=' ', quotechar='|')
