arr = []
prompt = int(input("Enter a number: "))
while prompt >= 0:
    arr.append(prompt)
    prompt = int(input("Enter a number: "))

print(sorted(arr))
