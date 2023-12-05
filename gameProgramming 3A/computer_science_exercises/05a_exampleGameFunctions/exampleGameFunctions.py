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


def getTeam(): # Function passes code test.  
    print('Welcome to the Intergalactic Card Game!\n')
    team = input(f'Before we get started, please input a number of the team you would like to be on:\n{teamSelect}\n')
    
    while team not in '1234':
        team = input('Team number not in range. Please input a number within 1-4 and press enter.\n')
    teamName = teamSelect[int(team)]
    # print(teamName)
    return teamName 

myTeam = getTeam()

def cardStatus(cardType): # Finish the if/elf/else block for the card types. 
    # while len(cardType) < 10:
    #     cardType = [random.randint(0, 4)]
    #     damageNumGen = random.randint(0, 50)
    #     moveSpeedGen = random.randint(0, 50)
    #     armorStatGen = random.randint(0, 10)
    #     baseHealthGen = random.randint(0, 100)
        
        

    if cardType == 'Artillery':
        damageNumGen = random.randint(0, 50)
        moveSpeedGen = random.randint(0, 50)
        armorStatGen = random.randint(0, 10)
        baseHealthGen = random.randint(0, 100)
    elif cardType == 'Infantry':
        damageNumGen = random.randint(0, 10)
        moveSpeedGen = random.randint(0, 10)
        armorStatGen = random.randint(0, 5)
        baseHealthGen = random.randint(0, 10)
    # elif Tank 
    # elif Ariel 
    else: 
        print('Error Message Here')
    card = (cardType,damageNumGen, moveSpeedGen, armorStatGen, baseHealthGen)
    print(card)

cardStatus('Artillery')
cardStatus('Infantry')

# while numCardsInDeck > 0: 
#     drawCard()
#     cardType = getCardType(card)
#     cardStatus(cardType) 

def makeDeck(cardType): 
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