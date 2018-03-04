import csv
from common import find_biggest_sum_in_dict


def branch_counter(f):
    csv_data = csv.reader(f, delimiter=",")
    next(csv_data)
    branch_counter = {}
    for row in csv_data:
        branch_counter.setdefault(row[3], 0)
        branch_counter[row[3]] += 1
    return branch_counter


def run(f):
    f.seek(0)
    branch_sums = branch_counter(f)
    result = find_biggest_sum_in_dict(branch_sums)
    print("The main Branch that people came from was: \"" + result["name"].lower().capitalize() +
          "\" with total count of " + str(result["sum"]) + ".")

#display duplicate info and total

#with open('korean_conflict.csv') as csvfile:
 #   reader = csv.DictReader(csvfile)
  #  for i,row in enumerate(reader):
   #     print(row['SERVICE_TYPE'], row['SERVICE_CODE'], row['ENROLLMENT'], row['BRANCH'], row['RANK'])
    #    if(i >= 9):
     #       break