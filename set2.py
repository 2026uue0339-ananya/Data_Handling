import csv

with open("candidates.csv", "r", newline="") as file:

    reader = csv.reader(file)
    next(reader)  # Skip the header row

    for row in reader:

        name = row[0]
        roll = int(row[1])
        marks = float(row[2])
        print("Name:", name)
        print("Roll Number:", roll)
        print("Marks:", marks)
        print("####################")
        

    print("Readable format ready!")    