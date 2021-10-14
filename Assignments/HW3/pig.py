import random

player = 0
computer = 0

while player < 50 and computer < 50:
    print(f"\nPlayer: {player}\nComputer: {computer}\n")

    print("HUMAN'S TURN-----------------------------------------")
    roll = random.randint(1,6)

    if roll != 1:
        playerSum = 0
        playerSum += roll
        action = input(f"\nRolled a {roll}\nroll or hold (r/h)?\n")
        print()
        while action[0].lower() not in "hr":
            action = input(f"\nPlease select to roll or hold the {roll} points (r/h)\n")

        while action.lower() != "h":
            roll = random.randint(1,6)
            if roll == 1:
                print("you have rolled a 1")
                playerSum = 0
                break
            else:
                playerSum += roll
                action = input(f"Rolled a {roll}\nroll or hold (r/h)?\n")
                print()
        player += playerSum
    else:
        print("You have rolled a 1: No points given\n")

    if player >= 50:
        break

    print("COMPUTER'S TURN--------------------------------------")

    roll = random.randint(1,6)
    compSum = 0
    while compSum < 20:
        roll = random.randint(1,6)
        if roll == 1:
            print("Computer rolled a 1: No points given\n")
            compSum = 0
            break
        else:
            if compSum + computer >= 50:
                computer += compSum
                break
            else:
                compSum += roll
    computer += compSum

winner = "Player" if (player >= 50 and computer < 50) else "Computer"
points = player if (player >= 50 and computer < 50) else computer
print(f"\nCongratulations {winner}!\nYou have won with {points} points!")
