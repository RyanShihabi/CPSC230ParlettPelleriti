initial = int(input("Enter a number: "))

sumConsec = 0

for x in range(initial, 0, -1):
    sumConsec += x

print(f"Consecutive sum: {sumConsec}")

# ------ For fun ------

def sumConsecRecursive(n):
    if n == 1:
        return 1
    else:
        return n + sumConsecRecursive(n-1)

print(sumConsecRecursive(initial))
