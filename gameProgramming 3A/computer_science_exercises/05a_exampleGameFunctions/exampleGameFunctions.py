# Example Game Functions, Gavin Kloeckner, v0.1.7 WIP
import random

damageNum = 0 # 0 min / 100 max
moveSpeed = 0 # 0 min / 100 max
armorStat = 0 # 0 min / 100 max 
baseHealth = 0 # 0 min / 100 max 
cardType = [
            "Infantry",
            "Artillery",
            "Tank",
            "Aerial"
]

teamSelect = ['Fake Team', 'Team 1', 'Team 2', 'Team 3', 'Team 4']


def getTeam(): # Function passes code test.  
    print('Welcome to the Intergalactic Card Game!\n')
    team = input(f'Before we get started, please input a number of the team you would like to be on:\n{teamSelect}\n')
    
    while team not in '1234':
        team = input('Team number not in range. Please input a number within 1-4 and press enter.\n')
    teamName = teamSelect[int(team)]
    # print(teamName)
    return teamName 

# myTeam = getTeam()

def cardStatus(cardType): # Finish the if/elf/else block for the card types. 
    if cardType == 'Artillery':
        damageNumGen = random.randint(40, 110)
        moveSpeedGen = random.randint(0, 30)
        armorStatGen = random.randint(0, 10)
        baseHealthGen = random.randint(10, 30)
    elif cardType == 'Infantry':
        damageNumGen = random.randint(1, 10)
        moveSpeedGen = random.randint(1, 15)
        armorStatGen = random.randint(1, 10)
        baseHealthGen = random.randint(1, 8)
    elif cardType == 'Tank':
        damageNumGen = random.randint(10, 50)
        moveSpeedGen = random.randint(10, 40)
        armorStatGen = random.randint(10, 80)
        baseHealthGen = random.randint(10, 70)
    elif 'Aerial':
        damageNumGen = random.randint(10, 30)
        moveSpeedGen = random.randint(40, 100)
        armorStatGen = random.randint(3, 30)
        baseHealthGen = random.randint(3, 20)
    else: 
        print('Unable to recognize cards.\n')
    card = (damageNumGen, moveSpeedGen, armorStatGen, baseHealthGen)
    print(card)
cardStatus(cardType)

# while numCardsInDeck > 0: 
#     drawCard()
#     cardType = getCardType(card)
#     cardStatus(cardType) 

def makeDeck(cardType, ):
    deckList = [] 
    while len(deckList) < 10: 
        deckList.append(cardType[random.randint(0, 3)])
    print(deckList)

makeDeck(cardType)

def shuffleDeck(cardList):
    pass

def dealCards(numCards, numPlayers): 
    pass


# Code Review by Lily King