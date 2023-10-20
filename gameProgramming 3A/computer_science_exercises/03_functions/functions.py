# Functions, 10-18-23, Gavin Kloeckner, v0.4.1

import random

# def functionName(): # Function Signature 
#     print("What is your name?\n")
#     name = input("Please type your name in the space below.\n")
#     print(f"Hello there {name}!\n")

# # Call The Function
# functionName()

# def happyBirthday(numTimes, age):
#     count = 0
#     while count < numTimes:
#         print("Happy Birthday!\n")
#     count += 1
#     print(f"Congratulations on turning {age}-years-old!\n")


# #happyBirthday(10, 36)

# def functionWithReturn(num1, num2):
#     sum = num1 + num2
#     quotient = sum / 5
#     return quotient # returns immediately exits a function

# def functionWithReturn(num1, num2):
#     sum = num1 + num2
#     quotient = sum / 5
#     print(quotient)

# example = functionWithReturn(4, 17)
# print(example)

def rollDice(numRoll, sizeRoll):
    count = 0
    sum = 0
    while count < numRoll:
        roll = random.randint(1, sizeRoll)
        # print(f"Roll #{count}: {roll}\n")
        sum += roll
        count += 1
    # print(sum)
    return sum

# print("D4 Rolls")
# d4Sum = rollDice(10, 4)
# print("D20 Rolls")
# d20Sum = rollDice(2, 20)

# print(d4Sum)
# print(d20Sum)

def genStat():
    rolls = [0, 0, 0, 0] 
    rolls[0] = rollDice(1, 6)
    rolls[1] = rollDice(1, 6)
    rolls[2] = rollDice(1, 6)
    rolls[3] = rollDice(1, 6)
    print(rolls)
    rolls.sort()
    rolls.pop(0)
    print(rolls)
    print(sum(rolls))


genStat()