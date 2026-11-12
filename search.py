import csv

search_roll = int(input("Enter the roll number to search: "))
found = False

with open("students.csv", "r", newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["RollNo"]) == search_roll:
            print("Student found!")
            print("Name:", row["Name"])
            print("Roll Number:", row["RollNo"])
            print("Marks:", row["Marks"])
            found = True
            break

if not found:
    print("Student with roll number", search_roll, "not found.")
