import csv

with open("results.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "RollNo", "Marks", "Status"])

    with open("students.csv", "r", newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for row in reader:
            name = row[0]
            roll = int(row[1])
            marks = float(row[2])

            if marks >= 40:
                status = "Pass"
            else:
                status = "Fail"

            writer.writerow([name, roll, marks, status])

        print("Results saved successfully!")    



