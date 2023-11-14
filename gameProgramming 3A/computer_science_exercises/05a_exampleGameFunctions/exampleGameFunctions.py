# Example Game Functions, Gavin Kloeckner, v0.0
import random

damageNum = 0
moveSpeed = 0
armorStat = 0
baseHealth = 0
cardType = 'Infantry Artillery Tank Aerial'.split()
teamSelection = 'CRYTINAN_EMPIRE HYPTION_UNION ALTRIAN_NATIONALISTS HARP\'TEKEN_FEDERATION'.split()

def startGame():
    print('Welcome to the Intergelactic Card Game!\n')
    while True:
        team = input(f'Before we get started, please select which team you would like to be on:\n{teamSelection}\n').upper()
        clarify = input(f'Are you sure you want to be on team {team}?\n')
        if clarify.upper().startswith('y'):
            print('Alright, now that you have selected your team,\nlet\'s move on.')
        else:
            print('Please select what team you want to be on.\n')

    return

startGame()

def cardStatus(damageNum, moveSpeed, armorStat, baseHealth, cardType, cardSelection):
    while len(cardType) > 10:
        pass