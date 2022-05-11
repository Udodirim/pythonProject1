import csv

with open('titanic.csv') as file:
    csv_reader = csv.reader(file)
    headings = next(csv_reader)
    first_value = next(csv_reader)
    print(headings)
    print(first_value)
    first_five_values = file.readlines(5)
    print(first_five_values)
    # for record in csv_reader:
    #     print(record[3])
