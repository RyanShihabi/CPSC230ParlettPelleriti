import random

# comparator function with two integer inputs that return an integer
def comparator(a: int, b: int) -> int:
    # return 1 if a is greater than b
    if a > b:
        return 1
    # return -1 if a is less than b
    elif a < b:
        return -1
    # otherwise return 0
    else:
        return 0

# function to give feedback to user with an integer parameter
def remark(val: int):
    # if value from comparator is 1
    if val == 1:
        print("You guessed higher!")
    # if value from comparator is -1
    elif val == -1:
        print("You guessed lower!")
    # if the guessed value and answer are the same
    else:
        print("You got it!")
        # gives the while loop something to end
        return 0

# user input function that returns and integer
def guess() -> int:
    val = input("Guess a number from 0 to 100: ")
    while not val.isnumeric() and (0 <= int(val) <= 100):
        val = input("Enter a number from 0 to 100: ")

    return int(val)

def main():
    # grab user guess
    user_guess = guess()
    # get number from 0 to 100
    number = random.randint(0, 100)

    # continue to guess until remark of comparator is 0
    while remark(comparator(user_guess, number)) != 0:
        user_guess = guess()


if __name__ == "__main__":
    main()
