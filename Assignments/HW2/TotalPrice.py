price, sales_tax = int(input("Item purchase price: ")), float(input("Sales tax rate of the item: "))

if price < 0:
    print("Please input a non-negative price value")
elif sales_tax < 0:
    print("Please input a rate that is not negative")
else:
    print(f"Total price: ${price+(price*sales_tax):.2f}")
