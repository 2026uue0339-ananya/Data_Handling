
import csv

books = [
    {"Book_Id": 1, "Title": "To Kill a Mockingbird", "Stock": 5},
    {"Book_Id": 2, "Title": "1984", "Stock": 3},
    {"Book_Id": 3, "Title": "The Great Gatsby", "Stock": 2},
    {"Book_Id": 4, "Title": "Pride and Prejudice", "Stock": 4}
]

# Create CSV file
with open("books.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["Book_Id", "Title", "Stock"]
    )
    writer.writeheader()
    writer.writerows(books)


exit = "no"

while exit != "yes":

    search_Id = int(input("Enter the Book_Id to search: "))
    quantity = int(input("Enter the quantity to check: "))

    # Read all records from CSV
    with open("books.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        books = list(reader)

    found = False

    # Search and update stock
    for row in books:

        if int(row["Book_Id"]) == search_Id:
            found = True

            if int(row["Stock"]) >= quantity:

                row["Stock"] = int(row["Stock"]) - quantity

                print("Book is available.")
                #print("Stock updated. New stock:", row["Stock"])

            else:
                print("Book is not available.")

            break

    if not found:
        print("Book with Book_Id", search_Id, "not found.")

    # Write updated records back to CSV
    with open("books.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Book_Id", "Title", "Stock"]
        )
        writer.writeheader()
        writer.writerows(books)

    exit = input("Do you want to exit? (yes/no): ")


##one learning: dont open writer in reeader if want to updaate any key values.
#  while reading just read chech conditions.after reading complete and  get out of loop 
# then start writing. or it will erase what has read.