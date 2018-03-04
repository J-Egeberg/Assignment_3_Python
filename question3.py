import csv


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


def print_biggest_ethnicity(ethnicity_sums):
    biggest_sum = 0
    biggest_ethnicity = ''
    for ethnicity, count in ethnicity_sums.items():
        if biggest_sum < count:
            biggest_ethnicity = ethnicity
            biggest_sum = count
    print("Major ethnicity was: \"" + biggest_ethnicity.lower().capitalize() +
          "\" with total count of " + str(biggest_sum) + ".")


def run(f):
    ethnicity_sums = sum_ethnicities(f)
    print_biggest_ethnicity(ethnicity_sums)