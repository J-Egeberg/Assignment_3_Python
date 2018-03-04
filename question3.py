import csv
from common import find_biggest_sum_in_dict


def sum_ethnicities(f):
    csv_data = csv.reader(f, delimiter=",")
    next(csv_data)
    ethnicity_counter = {}
    for row in csv_data:
        ethnicity_counter.setdefault(row[15], 0)
        ethnicity_counter[row[15]] += 1
        if row[15] != row[16] and row[16] != 'NOT SPECIFIED':
            ethnicity_counter.setdefault(row[16], 0)
            ethnicity_counter[row[16]] += 1
    return ethnicity_counter




def run(f):
    f.seek(0)
    ethnicity_sums = sum_ethnicities(f)
    result = find_biggest_sum_in_dict(ethnicity_sums)
    print("Major ethnicity was: \"" + result["name"].lower().capitalize() +
          "\" with total count of " + str(result["sum"]) + ".")