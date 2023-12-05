# Example Game Functions, Gavin Kloeckner, v0.1.6 WIP
import random

damageNum = 0 # Set min / max values, or describe the variable. 
moveSpeed = 0 # Set min / max values, or describe the variable. 
armorStat = 0 # Set min / max values, or describe the variable. 
baseHealth = 0 # Set min / max values, or describe the variable. 
cardType = [
            "Infantry",
            "Artillery",
            "Tank",
            "Aerial"
]

teamSelect = ['Fake Team', 'Team 1', 'Team 2', 'Team 3', 'Team 4']


def getTeam():
    print('Welcome to the Intergalactic Card Game!\n')
    team = input(f'Before we get started, please input a number of the team you would like to be on:\n{teamSelect}\n')
    
    while team not in '1234':
        team = input('Team number not in range. Please input a number within 1-4 and press enter.\n')
    teamName = teamSelect[int(team)]
    # print(teamName)
    return teamName 

myTeam = getTeam()

cardtype = []
def cardStatus(cardType):
    while len(cardType) < 10:
        cardType = [random.randint(0, 4)]
        damageNumGen = random.randint(0, 50)
        moveSpeedGen = random.randint(0, 50)
        armorStatGen = random.randint(0, 10)
        baseHealthGen = random.randint(0, 100)
        deck = (cardType,damageNumGen, moveSpeedGen, armorStatGen, baseHealthGen)
        
        print(deck)

#cardStatus(cardType)


# Code Review by Lily King