import csv

#we read into input.csv file
with open("input.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#we create output.csv containing the salaries computed
