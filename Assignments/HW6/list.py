arr = [["a", 7],["b", 8],["apple", "coin"]]
result_dict = {}

for x in range(len(arr)):
    result_dict[arr[x][0]] = arr[x][1]

print(result_dict)
