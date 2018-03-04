from file_handler import get_csv_sheet
import csv
import collections

#reader = get_csv_sheet()
#for row in reader:
#    print(row)


#define our data
with open(r"./korean_conflict.csv") as f:
    csv_data = csv.reader(f,delimiter=",")

#our counter
count = collections.Counter()

#first pass read the file
for row in csv_data:
    BRANCH = row[3]
    count[BRANCH] +=1

#display duplicate info and total
total_dups = 0
for BRANCH,nb in count.items():
    if nb>1:
        total_dups += nb
        print('{} is a duplicate branch, seen {} times'.format(BRANCH,nb))
    else:
        print('{} is a unique branch'.format(BRANCH))
print("Total duplicate branches {}".format(total_dups))


#with open('korean_conflict.csv') as csvfile:
 #   reader = csv.DictReader(csvfile)
  #  for i,row in enumerate(reader):
   #     print(row['SERVICE_TYPE'], row['SERVICE_CODE'], row['ENROLLMENT'], row['BRANCH'], row['RANK'])
    #    if(i >= 9):
     #       break