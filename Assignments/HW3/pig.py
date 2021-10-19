import random

# declaring initial score for player and computer
player = 0
computer = 0

# continue code until player or computer reaches 50+ points
while player < 50 and computer < 50:
    # Display points
    print(f"\nPlayer: {player}\nComputer: {computer}\n")

    # Player's turn
    print("HUMAN'S TURN-----------------------------------------")
    # Roll a number 1 to 6
    roll = random.randint(1,6)

    # check if initial roll was not one
    if roll != 1:
        # incrementing roll score until 1 is shown
        playerSum = 0
        playerSum += roll
        action = input(f"\nRolled a {roll}\nroll or hold (r/h)?\n")
        print()
        # prompting user if roll or hold is not specified
        while action[0].lower() not in "hr":
            action = input(f"\nPlease select to roll or hold the {roll} points (r/h)\n")

        # continue to roll if inputted
        while action.lower() != "h":
            roll = random.randint(1,6)
            # when user rolls a 1
            if roll == 1:
                # add no score to sum
                print("you have rolled a 1")
                playerSum = 0
                break
            else:
                playerSum += roll
                action = input(f"Rolled a {roll}\nroll or hold (r/h)?\n")
                print()
        # add roll sum to total points
        player += playerSum
    else:
        print("You have rolled a 1: No points given\n")

    # stop game if player has 50+ points
    if player >= 50:
        break

    # indicate computer's turn
    print("COMPUTER'S TURN--------------------------------------")

    # roll from 1 to 6
    compSum = 0
    # check if computer has less than 20 points
    while compSum < 20:
        roll = random.randint(1,6)
        # determine when computer rolls a 1
        if roll == 1:
            print("Computer rolled a 1: No points given\n")
            # dont reward any points
            compSum = 0
            break
        else:
            # check if computer has already won
            if compSum + computer >= 50:
                computer += compSum
                break
            else:
                # add roll to sum of current rolls
                compSum += roll
    computer += compSum

# calculating winner
winner = "Player" if (player >= 50 and computer < 50) else "Computer"
# calculating winning points
points = player if (player >= 50 and computer < 50) else computer
# prompt winner
print(f"\nCongratulations {winner}!\nYou have won with {points} points!")
