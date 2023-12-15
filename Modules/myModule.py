# Dice Roll, Gavin Kloeckner, v0.3.3

import random, time, tracemalloc

def rollDice(numRoll, sizeRoll):
    count = 0
    sum = 0
    while count < numRoll:
        roll = random.randint(1, sizeRoll)
        print(f"Roll #{count}: {roll}\n")
        sum += roll
        count += 1
    print(sum)
    return sum

# Verified to be working
def dispDice(numRoll, sizeRoll):
    count = 0
    sum = 0
    while count < numRoll:
        roll = random.randint(1, sizeRoll)
        print(f"Roll #{count}: {roll}\n")
        sum += roll
        count += 1
    print(sum)
    return sum

    
def isExploding(roll, sizeRoll):
    if roll == sizeRoll:
        isExploding = True
    else:
        isExploding = False
    return isExploding

# Code confirmed. It is working as intended.
def isDouble(roll1, roll2):
    if roll1 == roll2:
        isDouble = True
    else:
        isDouble = False
    return isDouble

roll1 = rollDice(1, 6)
roll2 = rollDice(1, 6)
print(f'The first roll is {roll1}.\nThe second roll is {roll2}.\n')

def getTime():
    return time.time()


def execTime(start, stop):
    return f'Execution Time: {start - stop} seconds.\n'

def memStart():
    return tracemalloc.start()

def memStop():
    return tracemalloc.stop()

def memUsage(start, stop):
    return f'Current Memory Usage: {start}\nHighest Memory Usage: {stop}\n'