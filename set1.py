import csv

with open("candidates.csv", "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow(["Name", "RollNo", "Marks"])

    for i in range(5):

        name = input("Enter candidate name: ")
        roll = int(input("Enter roll number: "))
        marks = float(input("Enter marks: "))

        writer.writerow([name, roll, marks])

    print("Candidate records saved successfully!")    