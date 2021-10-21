import random

def comparator(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

def remark(val):
    if val == 1:
        print("You guessed higher!")
    elif val == -1:
        print("You guessed lower!")
    else:
        print("You got it!")
        return 0

def guess():
    val = input("Guess a number from 0 to 100: ")
    while not val.isnumeric() and (0 <= int(val) <= 100):
        val = input("Enter a number from 0 to 100: ")

    return int(val)

def main():
    user_guess = guess()
    number = random.randint(0, 100)

    while remark(comparator(user_guess, number)) != 0:
        user_guess = guess()


if __name__ == "__main__":
    main()
