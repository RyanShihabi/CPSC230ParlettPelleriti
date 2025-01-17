import csv
import random

# setting stat variables
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

# reading player info
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

# prompting player
print("Welcome!")
print("Your options are\n")

# showing player options
for person in player_list:
    print(f"{person['Name']} the {person['Class']}")
    names.append(person["Name"])

# grabbing player selection
choice = input("\nWho would you like to play?\n")

# keep prompting until user chooses an existing player
while choice not in names:
    choice = input("\nOnly enter the name of who would you like to play?\n")

# grabbing a player for the computer
opponent = names[random.randint(0, len(names)-1)]
while opponent == choice:
    opponent = names[random.randint(0, len(names)-1)]

# assigning the player dictionary to the name
for person in player_list:
    if person["Name"] == opponent:
        selected["Opponent"] = person
    if person["Name"] == choice:
        selected["Player"] = person

print(f"Your opponent is {selected['Opponent']['Name']} the {selected['Opponent']['Class']}\n")

# iterating through weapons file
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

# Listing weapon info
for weapon in weapon_list:
    print(f"{weapon['Name']} which does {weapon['Damage_Min']} to {weapon['Damage_Max']} damage and is ideal for a {weapon['Ideal']}")
    weapon_names.append(weapon['Name'])

# asking for weapon choice
weapon_choice = input("\nChoose a weapon for your character: ")

# keep prompting until existing weapon is found
while weapon_choice not in weapon_names:
    weapon_choice = input("\nOnly enter the name to choose a weapon for your character: \n")

for weapon in weapon_list:
    if weapon["Name"] == weapon_choice:
        weapon_choice = weapon
        break

# making sure the weapon ideal class matches the class of the player
while weapon_choice["Ideal"] != selected["Player"]["Class"]:
    if weapon_choice["Name"] not in weapon_names:
        weapon_choice = input("\nOnly enter the name to choose a weapon for your character: ")
    else:
        weapon_choice = input("\nChoose a weapon that is ideal for your character: ")

    for weapon in weapon_list:
        if weapon["Name"] == weapon_choice:
            weapon_choice = weapon
            break

# assign weapon to player dictionary
selected["Player"]["Weapon"] = weapon_choice

# randomly assigning a weapon for the computer that also matches their ideal class
opponent_weapon = weapon_list[random.randint(0, len(weapon_list))-1]
while opponent_weapon == choice:
    opponent_weapon = weapon_list[random.randint(0, len(weapon_list)-1)]

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

# assigning weapon to opponent dictionary
selected["Opponent"]["Weapon"] = opponent_weapon

print(f"Opponent is using {selected['Opponent']['Weapon']['Name']}\n")

# iterating through armor file
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

# listing armor options
for armor in armor_list:
    print(f"{armor['Name']} which blocks {armor['Min_Block']} to {armor['Max_Block']} damage {armor['Chance']*100}% of the time")
    armor_names.append(armor['Name'])

# input for armor choice
armor_choice = input("\nChoose armor for your character: ")

# making sure choice exists
while armor_choice not in armor_names:
    armor_choice = input("\nOnly enter the name to choose armor for your character: \n")

for armor in armor_list:
    if armor["Name"] == armor_choice:
        armor_choice = armor
        break

selected["Player"]["Armor"] = armor_choice

# randomly selecting armor for computer
opponent_armor = armor_list[random.randint(0, len(armor_list)-1)]
while opponent_armor == choice:
    opponent_armor = armor_list[random.randint(0, len(armor_list)-1)]

for armor in armor_list:
    if armor["Name"] == opponent_armor:
        opponent_armor = armor
        break

while opponent_armor["Name"] == selected["Player"]["Armor"]["Name"]:
        opponent_armor = armor_list[random.randint(0, len(armor_list)-1)]
        for armor in armor_list:
            if armor["Name"] == opponent_armor:
                opponent_armor = armor
                break

selected["Opponent"]["Armor"] = opponent_armor

# checks if either player is still alive in battle
def still_alive(player):
    # array of death messages
    death_messages = [f"Oh no, {player['Name']} died", f"{player['Name']} has died", f"{player['Name']} has been defeated", f"{player['Name']} loses in combat", f"{player['Name']} falls to the ground", f"{player['Name']} dies honorably"]
    # check if health is 0
    if player["Health"] == 0:
        print(death_messages[random.randint(0, len(death_messages)-1)])
        return False
    return True

# goes over one round/iteration of the battle
def player_turn(selected, attack_special):
    # player 1
    damage = 0
    # calculating block chances for both players
    chance_block_opponent = random.uniform(0, 1)
    chance_block_player = random.uniform(0, 1)
    # when special attack is chosen
    if attack_special:
        # determine if cooldown is zero
        if selected["Player"]["Turns_Since"] == 0:
            print("\nSpecial Attack Used")
            # random heal chance
            heal = random.randint(0, 10)
            if heal <= 2:
                print("You have healed your opponent")
                damage = -2
            # assign random damage in range
            else:
                damage = random.randint(selected["Player"]["Special_Attack_Min"], selected["Player"]["Special_Attack_Max"])
                if chance_block_opponent < selected["Opponent"]["Armor"]["Chance"]:
                    damage_block = random.randint(selected["Opponent"]["Armor"]["Min_Block"], selected["Opponent"]["Armor"]["Max_Block"])
                    damage = max(0, damage-damage_block)
                    print(f"{selected['Opponent']['Name']} blocked {damage_block} damage")
            # assign health to zero if health becomes negative
            selected["Opponent"]["Health"] = max(0, min(100, selected["Opponent"]["Health"]-damage))
            # set cooldown to max
            selected["Player"]["Turns_Since"] = selected["Player"]["Cooldown"]
        else:
            print("\nSpecial Attack Attempted.")
            print("Basic Attack Used")
            # do random basic attack damage
            damage = random.randint(selected["Player"]["Weapon"]["Damage_Min"], selected["Player"]["Weapon"]["Damage_Max"])

            if chance_block_opponent < selected["Opponent"]["Armor"]["Chance"]:
                damage_block = random.randint(selected["Opponent"]["Armor"]["Min_Block"], selected["Opponent"]["Armor"]["Max_Block"])
                damage = max(0, damage-damage_block)
                print(f"{selected['Opponent']['Name']} blocked {damage_block} damage")

            # assign health to zero if health becomes negative
            selected["Opponent"]["Health"] = max(0, selected["Opponent"]["Health"]-damage)
            # decrease cooldown by one
            selected["Player"]["Turns_Since"] -= 1
    else:
        print("\nBasic Attack Used")
        # do random basic attack damage
        damage = random.randint(selected["Player"]["Weapon"]["Damage_Min"], selected["Player"]["Weapon"]["Damage_Max"])

        if chance_block_opponent < selected["Opponent"]["Armor"]["Chance"]:
            damage_block = random.randint(selected["Opponent"]["Armor"]["Min_Block"], selected["Opponent"]["Armor"]["Max_Block"])
            damage = max(0, damage-damage_block)
            print(f"{selected['Opponent']['Name']} blocked {damage_block} damage")

        # assign health to zero if health becomes negative
        selected["Opponent"]["Health"] = max(0, selected["Opponent"]["Health"]-damage)
        # decrease cooldown by one if not already at zero
        selected["Player"]["Turns_Since"] = max(0, selected["Player"]["Turns_Since"]-1)

    if damage < 0:
        print(f"\n{selected['Player']['Name']} healed 2 points this round!")
    else:
        print(f"\n{selected['Player']['Name']} did {damage} damage this round!")

    print(f"{selected['Opponent']['Name']} has {selected['Opponent']['Health']} HP left.\n")

    # stop function if player has reached zero health
    if still_alive(selected["Opponent"]) == False:
        return

    # computer
    # computer choice
    choice = random.randint(0, 1)
    # see if choice is 1
    if choice:
        # check if computer has no cooldown
        if selected["Opponent"]["Turns_Since"] == 0:
            print("\nSpecial Attack Used")
            # random heal chance
            heal = random.randint(0, 10)
            if heal <= 2:
                print("You have healed your opponent")
                damage = -2
            else:
                damage = random.randint(selected["Opponent"]["Special_Attack_Min"], selected["Opponent"]["Special_Attack_Max"])

                if chance_block_player < selected["Player"]["Armor"]["Chance"]:
                    damage_block = random.randint(selected["Player"]["Armor"]["Min_Block"], selected["Player"]["Armor"]["Max_Block"])
                    damage = max(0, damage-damage_block)
                    print(f"{selected['Player']['Name']} blocked {damage_block} damage")

            selected["Player"]["Health"] = max(0, min(100, selected["Player"]["Health"]-damage))
            selected["Opponent"]["Turns_Since"] = selected["Opponent"]["Cooldown"]
        # with a cooldown
        else:
            print("\nSpecial Attack Attempted.")
            print("Basic Attack Used")
            damage = random.randint(selected["Player"]["Weapon"]["Damage_Min"], selected["Player"]["Weapon"]["Damage_Max"])

            if chance_block_player < selected["Player"]["Armor"]["Chance"]:
                damage_block = random.randint(selected["Player"]["Armor"]["Min_Block"], selected["Player"]["Armor"]["Max_Block"])
                damage = max(0, damage-damage_block)
                print(f"{selected['Player']['Name']} blocked {damage_block} damage")

            selected["Player"]["Health"] = max(0, selected["Player"]["Health"]-damage)
            selected["Opponent"]["Turns_Since"] -= 1
    # basic attack
    else:
        print("\nBasic Attack Used")
        damage = random.randint(selected["Player"]["Weapon"]["Damage_Min"], selected["Player"]["Weapon"]["Damage_Max"])

        if chance_block_player < selected["Player"]["Armor"]["Chance"]:
            damage_block = random.randint(selected["Player"]["Armor"]["Min_Block"], selected["Player"]["Armor"]["Max_Block"])
            damage = max(0, damage-damage_block)
            print(f"{selected['Player']['Name']} blocked {damage_block} damage")

        selected["Player"]["Health"] = max(0, selected["Player"]["Health"]-damage)
        selected["Opponent"]["Turns_Since"] = max(0, selected["Opponent"]["Turns_Since"]-1)

    if damage < 0:
        print(f"\n{selected['Player']['Name']} healed 2 points this round!")
    else:
        print(f"\n{selected['Player']['Name']} did {damage} damage this round!")

    print(f"{selected['Player']['Name']} has {selected['Player']['Health']} HP left.\n")

    still_alive(selected["Player"])

round = 1

while selected["Player"]["Health"] > 0 and selected["Opponent"]["Health"] > 0:
    print(f"ROUND {round}---------------------\n")

    move = input("Select basic or special to attack: ").lower()

    while move not in ["basic", "special"]:
        move = input("Select 'basic' or 'special' to attack: ").lower()

    is_special = (move == 'special')

    player_turn(selected, is_special)

    round += 1

print(f"You are victorious!") if selected["Player"]["Health"] > 0 else print(f"Sorry player, {selected['Opponent']['Name']} is victorious!")
