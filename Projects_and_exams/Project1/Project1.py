import os
import requests
import json
import random

questions = json.loads(requests.get("https://opentdb.com/api.php?amount=2&type=boolean").text)
word = json.loads(requests.get("https://random-word-form.herokuapp.com/random/noun").text)[0]
# print(word)
# print(questions["results"][1]["question"])

d = {"n": {"north": "puzzle1", "east": "die", "south": "die", "west": "die"},
    "e": {"north": "puzzle3", "east": "die", "south": "die", "west": "die"},
    "s":{"north": "puzzle2", "east": "die", "south": "die", "west": "die"},
    "w": {"north": "puzzle4", "east": "die", "south": "die", "west": "die"}}

input_count = 0
dwarfs = ["doc", "bashful", "bneezy", "happy", "grumpy", "sleepy", "dopey"]

#welcome------------------------------
print("Welcome")
#choose character and opponent--------
user_name = input("What is your name: ")
#initial direction--------------------
direction = input(f"\nWhich direction do you want to go, {user_name}?\nN, S, E, or W?\nEnter: ").lower()
while direction not in "nsew":
    direction = input(f"Enter a valid direction\nN, S, E, or W\nEnter: ").lower()

path = d[direction]

question = questions["results"][input_count]["question"]
question = question.replace('&quot;', '"')
question = question.replace("&#039;", "'")
answer = questions["results"][input_count]["correct_answer"][0].lower()

user_input = input(f"\nTrue or False?\n{question}\nAnswer: ")

print("\nCorrect, nice job\n") if user_input[0].lower() == answer else print("\nIncorrect, that one was tough\n")

input_count += 1

#second direction---------------------

direction = input(f"Enter a new direction, {user_name}?\nNorth, South, East, or West \nEnter: ").lower()
while direction not in "northsoutheastwest":
    direction = input(f"Enter a valid direction\nNorth, South, East, or West\nEnter: ").lower()

question = questions["results"][input_count]["question"]
answer = questions["results"][input_count]["correct_answer"][0].lower()

user_input = input(f"\nTrue or False?\n{question}\nAnswer: ")

print("\nCorrect, nice job\n") if user_input[0].lower() == answer else print("\nIncorrect, that one was tough\n")

path = path[direction]
#---puzzles---------------------------
if path == "puzzle1":
    selected = []
    dwarf_input = input("Name one of the seven dwarfs: ").lower()
    while dwarf_input not in selected and dwarf_input in dwarfs:
        selected.append(dwarf_input)
        dwarf_input = input("Correct! Name another one: ")
    else:
        if len(selected) == 7:
            print("you got them all, congrats")
        else:
            print("you got it wrong")

    print("You have made it out alive")

elif path == "puzzle2":
    print("Rolling die...")
    number = random.randint(1,6)
    answer = input(f"Is the number {number} even or odd?").lower()
    if (answer[0] == "e" and number % 2 == 0) or (answer[0] == "o" and number % 2 != 0):
        print("Correct! You're smart")
    else:
        print("Incorrect")

    print("You have made it out alive")

elif path == "puzzle3":
    answer = input(f"Spell {word} backwards:\n")
    if answer != word[::-1]:
        print(f"False! Answer is {word[::-1]}")
    else:
        print("Good job!")

    print("You have made it out alive")

elif path == "puzzle4":
    answer = int(input("Enter a prime number: "))

    prime_count = 0
    for i in range(1, 10):
        if answer % i != 0:
            prime_count += 1
    if prime_count == 8:
        print("This is prime number")
    else:
        print("That is not a prime number")
    print("You have made it out alive")
else:
    print(f"Sorry, {user_name}, you have died")
    print("Here lies the end of your journey")

#end----------------------------------
