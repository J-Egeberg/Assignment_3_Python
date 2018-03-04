from file_handler import get_csv_sheet

reader = get_csv_sheet()
for row in reader:
    print(row)
