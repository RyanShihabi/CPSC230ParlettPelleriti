import csv
import random

player = {}
player_list = []
selected = {"Player": {}, "Opponent": {}}
columns = []
names = []

with open("players.csv", "r") as player_file:
    player_info = csv.reader(player_file, delimiter=",")
    line_count = 0
    for line in player_info:
        if line_count == 0:
            columns = ["Name"] + line[1:]
        else:
            for i in range(len(line)):
                if i <= 1:
                    player[columns[i]] = line[i]
                else:
                    player[columns[i]] = int(line[i])

            player_list.append(player)
            player = {}
        line_count += 1

player_file.close()

print("Welcome!")
print("Your options are\n")

for person in player_list:
    print(f"{person['Name']} the {person['Class']}")
    names.append(person["Name"])

choice = input("\nWho would you like to play?\n")

while choice not in names:
    choice = input("\nOnly enter the name of who would you like to play?\n")


opponent = names[random.randint(0, len(names))]
while opponent == choice:
    opponent = names[random.randint(0, len(names))]

for person in player_list:
    if person["Name"] == opponent:
        selected["Opponent"] = person
    if person["Name"] == choice:
        selected["Player"] = person

print(f"Your opponent is {selected['Opponent']['Name']} the {selected['Opponent']['Class']}")

print("Here are your weapon choices:")

# print(selected)
