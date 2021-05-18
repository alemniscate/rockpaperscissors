import random
import os

def get_score(username):
    if not os.path.exists("rating.txt"):
        return 0
    file = open("rating.txt", encoding="utf-8")
    lines = file.readlines()
    for line in lines:
        name, score = line.split()
        if username == name:
            return int(score)
    return 0

def game(score, options, alloptions):
    while True:
        user = input()
        if user in options:
            break
        if user == "!exit":
            return True, score
        if user == "!rating":
            print(f"Your rating: {score}")
            continue
        print("Invalid input")

    computer = random.choice(options)
    decision = get_decision(user, computer, alloptions)
    if decision == "draw":
        print(f"There is a draw ({user})")
        score += 50
    else:
        if decision == "computerwin":
            print(f"Sorry, but the computer chose {computer}")
        else:
            print(f"Well done. The computer chose {computer} and failed")
            score += 100

    return False, score

def get_decision(user, computer, alloptions):
    user_index = alloptions.index(user)
    computer_index = alloptions.index(computer)
    decision = user_index + 7 - computer_index
    if decision < 0:
        decision += 15
    if decision >= 15:
        decision -= 15

    if decision == 7:
        return "draw"
    elif decision < 7:
        return "userwin"
    elif decision > 7:
        return "computerwin" 

alloptions = ["rock","fire","scissors","snake","human","tree","wolf","sponge","paper","air","water","dragon","devil","lightning","gun"]

username = input("Enter your name: ")
print(f"Hello, {username}")
options = input()
if options == "":
    options = ["rock","paper","scissors"]
else:
    options = options.split(",")    
print("Okay, let's start")
score = get_score(username)

while True:
    exitflag, score = game(score, options, alloptions)
    if exitflag:
        break

print("Bye!")