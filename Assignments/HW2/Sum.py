amount = int(input("How many numbers would you like to enter?\n"))

while(amount <= 0):
    amount = int(input("How many numbers would you like to enter?\n"))

sum = 0

for x in range(amount):
    num = int(input("Enter a number: "))
    sum += num

print(f"Total: {sum}")
