import random

player = 0
computer = 0

while player < 100 and computer < 100:
    print(f"\nPlayer: {player}\nComputer: {computer}\n")

    print("Player's turn")
    roll = random.randint(1,6)

    if roll != 1:
        playerSum = 0
        playerSum += roll
        action = input(f"\nRolled a {roll}, roll or hold (r/h)?\n")
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
                action = input(f"Rolled a {roll}, roll or hold (r/h)?\n")
                print()
        player += playerSum
    else:
        print("You have rolled a 1\n")

    print("Computer's turn")

    roll = random.randint(1,6)
    compSum = 0
    while compSum < 20:
        roll = random.randint(1,6)
        if roll == 1:
            compSum = 0
            break
        else:
            if compSum + computer >= 100:
                computer += compSum
                break
            else:
                compSum += roll
    computer += compSum

winner = "Player" if (player >= 100 and computer < 100) else "Computer"
points = player if (player >= 100 and computer < 100) else computer

print(f"\nWinner: {winner} with {points} points\n")
