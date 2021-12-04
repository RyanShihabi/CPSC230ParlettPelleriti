import csv
import random

player = {}
weapon = {}
armor = {}
player_list = []
selected = {"Player": {}, "Opponent": {}}
columns = []
names = []
weapon_list = []
weapon_names = []
armor_list = []
armor_names = []
cancelled = []

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

opponent = names[random.randint(0, len(names)-1)]
while opponent == choice:
    opponent = names[random.randint(0, len(names)-1)]

for person in player_list:
    if person["Name"] == opponent:
        selected["Opponent"] = person
    if person["Name"] == choice:
        selected["Player"] = person

print(f"Your opponent is {selected['Opponent']['Name']} the {selected['Opponent']['Class']}\n")

with open("weapons.csv", "r") as weapon_file:
    weapon_info = csv.reader(weapon_file, delimiter=",")
    line_count = 0
    for line in weapon_info:
        if line_count == 0:
            columns = ["Name"] + line[1:]
        else:
            for i in range(len(line)):
                if i == 0 or i == len(line) - 1:
                    weapon[columns[i]] = line[i]
                else:
                    weapon[columns[i]] = int(line[i])

            weapon_list.append(weapon)
            weapon = {}
        line_count += 1

weapon_file.close()

print("Here are your weapon choices:")

# print(weapon_list)

for weapon in weapon_list:
    print(f"{weapon['Name']} which does {weapon['Damage_Min']} to {weapon['Damage_Max']} damage and is ideal for a {weapon['Ideal']}")
    weapon_names.append(weapon['Name'])

weapon_choice = input("\nChoose a weapon for your character: ")
while weapon_choice not in weapon_names:
    weapon_choice = input("\nOnly enter the name to choose a weapon for your character: \n")

for weapon in weapon_list:
    if weapon["Name"] == weapon_choice:
        weapon_choice = weapon
        break

while weapon_choice["Ideal"] != selected["Player"]["Class"]:
    if weapon_choice["Name"] not in weapon_names:
        weapon_choice = input("\nOnly enter the name to choose a weapon for your character: ")
    else:
        weapon_choice = input("\nChoose a weapon that is ideal for your character: ")

    for weapon in weapon_list:
        if weapon["Name"] == weapon_choice:
            weapon_choice = weapon
            break

selected["Player"]["Weapon"] = weapon_choice

opponent_weapon = weapon_list[random.randint(0, len(weapon_list))]
while opponent_weapon == choice:
    opponent_weapon = weapon_list[random.randint(0, len(weapon_list))]

for weapon in weapon_list:
    if weapon["Name"] == opponent_weapon:
        opponent_weapon = weapon
        break

while opponent_weapon["Ideal"] != selected["Opponent"]["Class"]:
        cancelled.append(opponent_weapon)
        opponent_weapon = weapon_list[random.randint(0, len(weapon_list)-1)]
        while opponent_weapon == selected["Player"]["Weapon"]["Name"] or opponent_weapon in cancelled:
            opponent_weapon = weapon_list[random.randint(0, len(weapon_list)-1)]

for weapon in weapon_list:
    if weapon["Name"] == opponent_weapon:
        opponent_weapon = weapon
        break

selected["Opponent"]["Weapon"] = opponent_weapon

print(f"Opponent is using {selected['Opponent']['Weapon']['Name']}\n")

with open("armor.csv", "r") as armor_file:
    armor_info = csv.reader(armor_file, delimiter=",")
    line_count = 0
    for line in armor_info:
        if line_count == 0:
            columns = ["Name"] + line[1:]
        else:
            for i in range(len(line)):
                if i == 0:
                    armor[columns[i]] = line[i]
                elif i < len(line)-1:
                    armor[columns[i]] = int(line[i])
                else:
                    armor[columns[i]] = float(line[i])

            armor_list.append(armor)
            armor = {}
        line_count += 1

armor_file.close()

print("Here are your armor material options")

for armor in armor_list:
    print(f"{armor['Name']} which blocks {armor['Block_Min']} to {armor['Block_Max']} damage {armor['Chance']*100}% of the time")
    armor_names.append(armor['Name'])

armor_choice = input("\nChoose armor for your character: ")
while armor_choice not in armor_names:
    armor_choice = input("\nOnly enter the name to choose armor for your character: \n")

for armor in armor_list:
    if armor["Name"] == armor_choice:
        armor_choice = armor
        break

selected["Player"]["Armor"] = armor_choice

print(selected["Player"]["Armor"])
