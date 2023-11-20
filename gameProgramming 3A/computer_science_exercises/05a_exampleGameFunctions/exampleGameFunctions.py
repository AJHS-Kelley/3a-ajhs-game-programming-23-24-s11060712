# Example Game Functions, Gavin Kloeckner, v0.1.2
import random

damageNum = 0
moveSpeed = 0
armorStat = 0
baseHealth = 0
cardAmount = 0
cardType = 'Infantry Artillery Tank Aerial'.split()
teamSelection = 'CRYTINAN_EMPIRE HYPTION_UNION ALTRIAN_NATIONALISTS HARP\'TEKEN_FEDERATION'.split()

def startGame():
    print('Welcome to the Intergelactic Card Game!\n')
    team = input(f'Before we get started, please select which team you would like to be on:\n{teamSelection}\n').upper()
    while team not in teamSelection:
        clarify = input('Please select an item from the list and press enter.\n')
    while True:
        clarify = input(f'Are you sure you want to be on team {team}?\n')
        if clarify == 'yes':
            print('Alright, now that you have selected your team,\nlet\'s move on.')
            break
        else:
            team = input(f'Please select what team you want to be on:\n{teamSelection}\n').upper()


startGame()

def cardStatus(cardType, cardSelection):
    while len(cardSelection) > 10:
        print(cardType)

cardStatus()