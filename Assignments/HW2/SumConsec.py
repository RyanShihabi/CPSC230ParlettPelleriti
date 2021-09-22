# grabbing intitial number
x = int(input("Enter a number: "))
# This is for the recursive way
recursive = x
# declaring sumConsec to store result
sumConsec = 0

# execute if initial is greater than 0
while x > 0:
    # increment sumConsec by the initial
    sumConsec += x
    # decrement initial by one for next loop
    x -= 1

# print the total of sumConsec
print("Consecutive sum:", sumConsec)

# ------ For fun -------

# Function that takes an int parameter and returns an int
def sumConsecRecursive(x: int) -> int:
    # define a base case to end stack of calculations
    if x == 1:
        # base case returns 1
        return 1
    else:
        # calculate parameter value + the recursive sum of the number one less the parameter
        return x + sumConsecRecursive(x-1)

# print recrusive total of sum
print("-"*5, "for fun", "-"*5)
print("Recursive Sum:", sumConsecRecursive(recursive))
