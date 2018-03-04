import csv
from common import find_biggest_sum_in_dict

def sum_enrollment(f):
    csv_data = csv.reader(f, delimiter=",")
    next(csv_data)
    enrollment_counter = {}
    for row in csv_data:
        if row[2] != "":
            enrollment_counter.setdefault(row[2], 0)
            enrollment_counter[row[2]] += 1
    return enrollment_counter


def run(f):
    f.seek(0)
    division_sums = sum_enrollment(f)
    result = find_biggest_sum_in_dict(division_sums)
    print("The most common enrollment type was: \"" + result["name"].lower().capitalize() +
          "\" with total number of " + str(result["sum"]) + ".")