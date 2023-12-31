# Collections, Kloeckner Gavin, v0.4.4
# Adding items

# playerInventory = []
# while len(playerInventory) < 10:
#     item = input("What would you like to add?\n")
#     playerInventory.append(item)
# playerInventory.sort()
# # .whatever() is known as a method. It means "do this to that".
# print(playerInventory)

# # Removing Items
# while len(playerInventory) > 5:
#     item = input("Now, please select the item that you would like to remove from the inventory.\n")
#     playerInventory.remove(item)
# playerInventory.sort()
# print(playerInventory)

# weaponList = [
#     True, # Crytinan Standard Issue RaL-TC
#     True, # Personal Combat Sidearm-17 (PCS-17)
#     True, # V3 Impulse Grenade
#     False, # Energy Shield
#     False  # ARK-56 (Flame Launcher)
# ]
# # each item in the list is called an element, the location of each element is called an
# #index
# # first element is index[0]
# # shortcut to the last element is index[-1]
# weaponNum = 0
# while weaponNum < len(weaponList):
#     if weaponNum == 0 and weaponList[0] == True:
#         print("You have been outfitted with the RaL-TC.\n")
#     if weaponNum == 1 and weaponList[1] == True:
#         print("You have been outfitted with the PCS-17.\n")
#     if weaponNum == 2 and weaponList[2] == True:
#         print("You have been outfitted with the Impulse Grenade.\n")
#     if weaponNum == 3 and weaponList[3] == True:
#         print("You have been outfitted with the Energy Shield.\n")
#     if weaponNum == 4 and weaponList[4] == True:
#         print("You have been outfitted with the Flame Launcher.\n")
#     weaponNum += 1

# doorKeys = [
#     "red",
#     "blue",
#     "green",
#     "purple",
#     "white"
# ]
# color = input("Which key do you need to proceed?\n").lower()
# if color in doorKeys:
#     print(f"You have the {color} key!.\n")
# else:
#     print(f"You do not have the {color} key.\n")

# Random Enemy Genrator

enemyBase = [
    "Soldier",
    "Artillery",
    "Tank",
    "RAV",
    "Dropship",
    "Fighter"
]

enemyType = [
    "Front Line Infantry",
    "Heavy Artillery Piece",
    "Hover Tank",
    "Orbital Dropship",
    "Ravager Star Fighter"
]

enemyPrefix = [
    "Standard Unit",
    "Mobile Support Unit",
    "Heavy Unit",
    "Light Reconaissence Vehicle",
    "Rapid Attack Vehicle"
]

import random

# Index Range (0,4)
enemyNames = [] 
while len(enemyNames) < 15:
    enemyBaseGen = enemyBase[random.randint(0,4)]
    enemyTypeGen = enemyType[random.randint(0,4)]
    enemyPrefixGen = enemyPrefix[random.randint(0,4)]
    newEnemy = enemyPrefixGen + " " + enemyBaseGen + " " + enemyTypeGen
    enemyNames += enemyBaseGen
    enemyNames.append(newEnemy)

print(enemyNames)