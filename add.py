import csv

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)

    
    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))

    writer.writerow([name, roll, marks])

    print("new student records added successfully!")