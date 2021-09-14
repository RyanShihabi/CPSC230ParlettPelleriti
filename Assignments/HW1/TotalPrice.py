# Price and sales_tax prompts
price, sales_tax = int(input("Item purchase price: ")), float(input("Sales tax rate of the item: "))

# print a formatted string with the result rounded to two decimal places
print(f"Total price: ${price + (price * sales_tax):.2f}")
