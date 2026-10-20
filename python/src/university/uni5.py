import random
from math import sqrt

print(sqrt(9))

grades = [9, 7, 7, 10, 3, 9, 6, 6, 2]

# grades[-1] = 4
# print(grades)

# print(max(grades))

# grades.sort()
# print(grades)

# print(sum(grades) / len(grades))

words = ("Sonic", "Tails", "Knuckles", "Amy", "Robotnik")

for word in words:
    print(f"\nWord: {word.upper()}. Vowels:")
    for letter in word:
        if letter.lower() in 'aeiou':
            print(letter.upper(), end=' ')

def valid_int(question, min, max):
    while True:
        try:
            x = int(input(question))
            if (x >= min) and (x <= max):
                return x
            else:
                print("Value out of range.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def winner(player1, player2):
    global v1, v2, draw
    if player1 == 1: # Stone
        if player2 == 1: # Stone
            draw += 1
        elif player2 == 2: # Paper
            v2 += 1
        elif player2 == 3: # Scissors
            v1 += 1
    elif player1 == 4: # Paper
        if player2 == 1: # Stone
            v1 += 1
        elif player2 == 2: # Paper
            draw += 1
        elif player2 == 3: # Scissors
            v2 += 1
    elif player1 == 5: # Scissors
        if player2 == 1: # Stone
            v2 += 1
        elif player2 == 2: # Paper
            v1 += 1
        elif player2 == 3: # Scissors
            draw += 1

    results = [v1, v2, draw]
    return results

print("JOKEMPO")
print("1 - Agent Stone")
print("2 - Flicky")
print("3 - Robotnik")

games = []
results = []
v1 = 0
v2 = 0
draw = 0

while True:
    j1 = valid_int("Choose your game: ", 0, 3)
    if not j1:
        break
    j2 = random.randint(1, 3)
    games.append([j1, j2])
    results = winner(j1, j2)

for game in games:
    for data in game:
        print(data, end = ' ')
    print()

print(f"Number of winnings from Player 1: {results[0]}.")
print(f"Number of winnings from Player 2: {results[1]}.")
print(f"Number of draws: {results[2]}.")

registration = {"name": [], "gender": [], "year": []}

while True:
    finish = input("You desire to register a clown? (Y/N)")
    if finish.upper() == "N":
        break
    if finish.upper() not in "Y":
        print("Type Y to say YAHYAHYAHYAHYAH and N to say NOOK")
        continue

    name = input("What's your silly name? ")
    gender = input("What's ur gender? ")
    year = input("What's ur birth certificate, baby? ")
    registration["name"].append(name)
    registration["gender"].append(gender.upper())
    registration["year"].append(year)

print(registration)

print("Welcome to the fucking dark web, what do you want to buy: ")
print("1 - Illegal stuff")
print("2 - Weapons")
print("3 - Cocaine")

product = int(input("What's your choice? "))
amount = int(input("How many? "))

match (product):
    case 1:
        pay = amount * 2.3
        print(f"You bought {amount} illegal stuff, good luck with that!")
    case 2:
        pay = amount * 7.5
        print(f"You bought {amount} weapons, good luck with that!")
    case 3:
        pay = amount * 15.5
        print(f"You bought {amount} kg of cocaine, good luck with that!")
    case _:
        print("Invalid input. You're now holding explosives.")
