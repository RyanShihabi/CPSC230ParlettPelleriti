# getting amount of numbers to enter
amount = int(input("How many numbers would you like to enter?\n"))
# declaring sum value
sum = 0

# while checks if amount goes over each value until none are left
while amount > 0:
    # get a number to add
    num = int(input("Enter a number to add: "))
    # increment sum by inputted num
    sum += num
    # decrement amount by 1
    amount -= 1

# print total of sum
print("Total:", sum)
