# Example Game Functions, Gavin Kloeckner, v0.1.4
import random

damageNum = 0
moveSpeed = 0
armorStat = 0
baseHealth = 0
cardAmount = 0
cardType = 'Infantry Artillery Tank Aerial'.split()
teamSelect = ['Team 1', 'Team 2', 'Team 3', 'Team 4']


# def getTeam():
#     print('Welcome to the Intergelactic Card Game!\n')
#     team = input(f'Before we get started, please input a number of the team you would like to be on:\n{teamSelect}\n')
#     while True:
#         if team not in '1234':
#             team = input('Team number not in range. Please input a number within 1-4 and press enter.\n')
#         elif team in '12345':
#             clarify = input(f'Are you sure you want to be on {team}?\n')
#         if clarify == 'yes':
#             print('Alright, now that you have selected your team,\nlet\'s move on.')
#             break
#         else:
#             team = input(f'Please select what team you want to be on:\n{teamSelect}\n')

# getTeam()

def cardStatus(cardType, cardAmount):
    while cardAmount < 10:
        cardType = cardType[random.randint(0,3)]
        damageNum = random.randint(0,50)
        moveSpeed = random.randint(0,50)
        armorStat = random.randint(0,10)
        baseHealth = random.randint(0,100)
        deck = cardType + damageNum + moveSpeed + armorStat + baseHealth
        cardType += deck
        cardAmount.append(deck)

cardStatus(cardType, cardAmount)


# Code Review by Lily King