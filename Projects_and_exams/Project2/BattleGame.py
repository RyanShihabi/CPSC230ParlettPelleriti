import random

# Step 9
def still_alive(player):
    # array of death messages
    death_messages = [f"Oh no, {player[0]} died", f"{player[0]} has died", f"{player[0]} has been defeated", f"{player[0]} loses in combat", f"{player[0]} falls to the ground", f"{player[0]} dies honorably"]
    # check if health is 0
    if player[3] == 0:
        print(death_messages[random.randint(0, len(death_messages)-1)])
        return False
    return True

# Step 7
def player_turn(attacker, defender, attack_special):
    # player 1
    damage = 0
    # when special attack is chosen
    if attack_special:
        # determine if cooldown is zero
        if attacker[5] == 0:
            print("\nSpecial Attack Used")
            # assign random damage in range
            damage = random.randint(attacker[2][0], attacker[2][1])
            # assign health to zero if health becomes negative
            defender[3] = max(0, defender[3]-damage)
            # set cooldown to max
            attacker[5] = attacker[4]
        else:
            print("\nSpecial Attack Attempted.")
            print("Basic Attack Used")
            # do random basic attack damage
            damage = random.randint(0, 6)
            # assign health to zero if health becomes negative
            defender[3] = max(0, defender[3]-damage)
            # decrease cooldown by one
            attacker[5] -= 1
    else:
        print("\nBasic Attack Used")
        # do random basic attack damage
        damage = random.randint(0, 6)
        # assign health to zero if health becomes negative
        defender[3] = max(0, defender[3]-damage)
        # decrease cooldown by one if not already at zero
        attacker[5] = max(0, attacker[5]-1)

    print(f"\n{attacker[0]} did {damage} damage this round!")

    print(f"{defender[0]} has {defender[3]} HP left.\n")

    # stop function if player has reached zero health
    if still_alive(defender) == False:
        return


    # computer
    # Step 8
    # computer choice
    choice = random.randint(0, 1)
    # see if choice is 1
    if choice:
        # check if computer has no cooldown
        if defender[5] == 0:
            print("\nSpecial Attack Used")
            damage = random.randint(defender[2][0], defender[2][1])
            attacker[3] = max(0, attacker[3]-damage)
            defender[5] = defender[4]
        # with a cooldown
        else:
            print("\nSpecial Attack Attempted.")
            print("Basic Attack Used")
            damage = random.randint(0, 6)
            attacker[3] = max(0, attacker[3]-damage)
            defender[5] -= 1
    # basic attack
    else:
        print("\nBasic Attack Used")
        damage = random.randint(0, 6)
        attacker[3] = max(0, attacker[3]-damage)
        defender[5] = max(0, defender[5]-1)

    print(f"\n{defender[0]} did {damage} damage this round!")

    print(f"{attacker[0]} has {attacker[3]} HP left.\n")

    still_alive(attacker)



# Step 1: creating two lists
player1 = ["Merlin", "Wizzard", [25, 30], 100, 3, 0]
player2 = ["Varguk", "Orc", [20, 25], 100, 2, 0]

# initial round set
round = 1

# Step 2
print(f"Welcome to Battledome. You're playing {player1[0]} who is a {player1[1]}")
# Step 3
print(f"Your opponent is {player2[0]} the {player2[1]}\n")

# loop until a player has no health
while player1[3] > 0 and player2[3] > 0:
    # Step 4
    print(f"ROUND {round}---------------------\n")

    # Step 5
    move = input("Select basic or special to attack: ").lower()
    # Step 6
    while move not in ["basic", "special"]:
        move = input("Select 'basic' or 'special' to attack: ").lower()

    is_special = (move == 'special')

    player_turn(player1, player2, is_special)

    round += 1

# Step 10
print(f"You are victorious!") if player1[3] > 0 else print(f"Sorry player, {player2[0]} is victorious!")
