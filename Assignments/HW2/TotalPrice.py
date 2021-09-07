price, sales_tax = int(input("Item purchase price: ")), float(input("Sales tax rate of the item: "))

if price<0:
    print("Please input a price greater than 0")
elif sales_tax<0:
    print("Please input a rate greater than 0")
else:
    print(f"Total price: ${price+(price*sales_tax):.2f}")
