import csv

with open("candidates.csv", "a", newline="") as file:
    writer = csv.writer(file)

    name = input("Enter candidate name: ")
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))

    with open("candidates.csv", "r", newline="") as read_file:
        reader = csv.reader(read_file)
        next(reader)  # Skip the header row

        #none of roll number can match with each other
        
        for row in reader:
            if int(row[1]) == roll:
                print("Error: Roll number already exists. Please enter a unique roll number.")
                name = input("Enter candidate name: ")
                roll = int(input("Enter roll number: "))
                marks = float(input("Enter marks: "))


    writer.writerow([name, roll, marks])

    print("New candidate record added successfully!")