initial = int(input("Enter a number: "))

sumConsec = 0

for x in range(initial, 0, -1):
    sumConsec += x

print(f"Consecutive sum: {sumConsec}")
