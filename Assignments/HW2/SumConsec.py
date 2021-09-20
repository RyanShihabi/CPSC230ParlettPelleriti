initial = int(input("Enter a number: "))
recursive = initial

sumConsec = 0

while initial > 0:
    sumConsec += initial
    initial -= 1

print("Consecutive sum:", sumConsec)

# ------ For fun ------

def sumConsecRecursive(n):
    if n == 1:
        return 1
    else:
        return n + sumConsecRecursive(n-1)

print("Recursive Sum:", sumConsecRecursive(recursive))
