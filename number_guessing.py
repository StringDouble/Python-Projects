#Copyright Yoana Stankova 2018
from random import randint

rand = (randint(1, 100))
while True:
    guess = input("What is the number?")


    if (int(guess) == rand):
        print("Yayy!")
        print("That is the number!")
        break

    elif (int(guess) < rand):
        print("The number is higher.\n")
        
        continue
    elif (int(guess) > rand):
        print("The number is lower.\n")
        continue
