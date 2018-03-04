import csv
from common import find_biggest_sum_in_dict


def sum_home_state(f):
    csv_data = csv.reader(f, delimiter=",")
    next(csv_data)
    home_state_counter = {}
    for row in csv_data:
        home_state_counter.setdefault(row[13], 0)
        home_state_counter[row[13]] += 1
    return home_state_counter


def run(f):
    f.seek(0)
    ethnicity_sums = sum_home_state(f)
    result = find_biggest_sum_in_dict(ethnicity_sums)
    print("The home state with the most casualties was: \"" + result["name"].lower().capitalize() +
          "\" with total count of " + str(result["sum"]) + ".")