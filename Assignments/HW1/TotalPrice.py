price, sales_tax = int(input("Item purchase price: ")), float(input("Sales tax rate of the item: "))

print(f"Total price: ${price+(price*sales_tax):.2f}")
