import csv

products = [
    {"Product": "Laptop", "Price": 50000, "Stock":5},
    {"Product": "Mouse", "Price": 500, "Stock":20},
    {"Product": "Keyboard", "Price": 1200, "Stock":10}
]

# write dictionary records to CSV

with open("products.csv", "w", newline='') as file:
    fieldnames = ["Product", "Price", "Stock"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(products)

print("products saved")    


#read dictionary records from CSV
with open("products.csv", "r", newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["Product"]
        price = float(row["Price"])
        stock = int(row["Stock"])
        print("Product:", product)
        print("Price:", price)
        print("Stock:", stock)
        print("--------------------")