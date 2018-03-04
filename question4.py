import csv
from common import find_biggest_sum_in_dict


def sum_divisions(f):
    csv_data = csv.reader(f, delimiter=",")
    next(csv_data)
    division_counter = {}
    for row in csv_data:
        if row[18] != "":
            division_counter.setdefault(row[18], 0)
            division_counter[row[18]] += 1
    return division_counter


def run(f):
    f.seek(0)
    division_sums = sum_divisions(f)
    result = find_biggest_sum_in_dict(division_sums)
    print("Division with most casualties was: \"" + result["name"].lower().capitalize() +
          "\" with total number of " + str(result["sum"]) + ".")