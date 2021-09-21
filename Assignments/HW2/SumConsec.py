# grabbing intitial number
initial = int(input("Enter a number: "))
# This is for the recursive way
recursive = initial
# declaring sumConsec to store result
sumConsec = 0

# execute if initial is greater than 0
while initial > 0:
    # increment sumConsec by the initial
    sumConsec += initial
    # decrement initial by one for next loop
    initial -= 1

# print the total of sumConsec
print("Consecutive sum:", sumConsec)

# ------ For fun -------

# Function that takes an int parameter and returns an int
def sumConsecRecursive(n: int) -> int:
    # define a base case to end stack of calculations
    if n == 1:
        # base case returns 1
        return 1
    else:
        # calculate parameter value + the recursive sum of the number one less the parameter
        return n + sumConsecRecursive(n-1)

# print recrusive total of sum
print("Recursive Sum:", sumConsecRecursive(recursive))
