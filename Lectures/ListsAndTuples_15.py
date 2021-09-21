# lists
l = ["Tan", "Antoni", "Karamo", "Jonathan", "Bobby"]

for fab in l:
    print("I love", fab)

x = [1,2,3,4,5,6]

for i in x:
    print(i**2)


days = ["Monday",
"Tuesday",
"Wednesday",
"Thursday",
"Friday",
"Saturday",
"Sunday"]

for day in days:
    if day == "Tuesday":
        print("it's taco time")

# indexing
print(days[0])
print(l[2:4])
print(l[::-1])

# mutability
l[0] = "Tim"
print(l)

# nested lists
spreadsheet = [["Name", "Age", "GPA"],
["Bill", 7, 0.0],
["Chelsea", 24,  4.0],
["Tony", 23, 3.7]]

## how do I grab "Bill"?
print(spreadsheet[3][2])


# tuples
my_tup = (1,2,3,4,5)

print(my_tup[0])

my_tup[0] = 0

# looping through more complex lists

spreadsheet = [["Name", "Age", "GPA"],
["Bill", 7, 0.0],
["Chelsea", 24,  4.0],
["Tony", 23, 3.7]]

for row in spreadsheet:
    for cell in row:
        print(cell)
