amount = int(input("How many numbers would you like to enter?\n"))
sum = 0

while amount > 0:
    num = int(input("Enter a number to add: "))
    sum += num
    amount -= 1

print(f"Total: {sum}")
