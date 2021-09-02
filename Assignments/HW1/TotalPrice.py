# grabbing price(integer) and sales tax(float) input
price, sales_tax = int(input("Item purchase price: ")), float(input("Sales tax rate of the item: "))

# outputting total price rounded to two decimal places all in a format string
print(f"Total price: ${price+(price*sales_tax):.2f}")
