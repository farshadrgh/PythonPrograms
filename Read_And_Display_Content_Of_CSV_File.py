import csv

# Put your file instead of ExampleFile.csv
reader = csv.reader(open("ExampleFile.csv"))

for row in reader:
    print(row)
