import csv
import requests
import os.path
import shutil


def download_file(file_name, url):
    split = url.split("/")
    original_file_name = split[len(split) - 1]
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        print("Downloaded " + file_name)
        with open(original_file_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
            os.rename("./" + original_file_name, "./" + file_name)


def download_csv_sheet():
    csv_sheet_name = "korean_conflict.csv"
    if not os.path.exists("./" + csv_sheet_name):
        download_file(csv_sheet_name,
                      "https://raw.githubusercontent.com/PatrickFenger/pythonAssignments/master/KoreanConflict.csv")
    return csv_sheet_name


def get_csv_sheet():
    csv_sheet_name = "korean_conflict.csv"
    if not os.path.exists("./" + csv_sheet_name):
        download_file(csv_sheet_name, 'https://raw.githubusercontent.com/PatrickFenger/pythonAssignments/master'
                                      '/KoreanConflict.csv')
    csvfile = open(csv_sheet_name)
    return csv.reader(csvfile, delimiter=' ', quotechar='|')
