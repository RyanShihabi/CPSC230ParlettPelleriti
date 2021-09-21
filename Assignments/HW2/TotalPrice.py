# get input for price and sales tax
price, sales_tax = int(input("Item purchase price: ")), float(input("Sales tax rate of the item: "))

# price and sales tax can be checked individually as only one value needs to be negative to ruin calculation

# check if price is negative
if price < 0:
    print("Calculation Error: Please input a non-negative price value")
# check if sales_tax is negative
elif sales_tax < 0:
    print("Calculation Error: Please input a rate that is not negative")
# when both values are positive
else:
    # use a format string to display calulated value rounded to two decimal places
    print(f"Total price: ${price+(price*sales_tax):.2f}")
