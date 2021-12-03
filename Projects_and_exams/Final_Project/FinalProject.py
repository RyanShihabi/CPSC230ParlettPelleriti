import csv

player = {}
player_list = []
selected = []
columns = []

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

choice = input("\nWho would you like to play?")
