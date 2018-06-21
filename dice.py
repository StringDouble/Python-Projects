#Copyright Yoana Stankova 2018
from random import randint

while True:
    print(randint(1, 6))
    roll = input("Do you want to roll again?")
    if (roll == "yes"):
        continue
    elif (roll == "no"):
        print("okay")
        break
    else:
        print("invalid syntax")
        break



