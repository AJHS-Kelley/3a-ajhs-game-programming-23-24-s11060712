# Pick a seceret number from a range for the possible numbers.
# Player guesses the number.
# Compare the guess to the seceret number.
# First player to score at least 6 points is declared the winner.
    # If the guess is correct, what should happen?
     # Award the player a point.
        #Print a "win" message on the screen.
    # If the guess is incorrect, what should happen?
        # Indicate if the guess is high/low compared to the seceret number.
    # Provide the player x number of guesses, based on range of numbers.
    # If the player does not guess correctly before hitting the limit, what happens?
        # Award a point to the CPU.
        # Print a loss message.

# INCORRECT FILE NAMES FOR IMAGES, CAUSES A CRASH. PLEASE FIX. 
# Guess a Number, Gavin Kloeckner, v0.7
import random, tracemalloc, winsound
from PIL import Image
tracemalloc.start()

# Declarations
secretNumber = -1 
playerName = "" # empty string
playerScore = 0
cpuScore = 0
numberOfGuesses = 0 
playerGuess = -1
userDifficulty = None
numAttempts = None
rangeMin = -1
rangeMax = -1

loserSound = 'sfx/numberGuess/losersound.wav'
winnerSound = 'sfx/numberGuess/winnersound.wav'

imageWin = Image.open('img/numberGuess/win.jpg')
imageLoss = Image.open('img/numberGuess/loser.jpg')


print("""
      
      
         #--------------------------------------#     
         |                                      |
         |                *MENU*                |
         |                                      |
         |          By: Gavin Kloeckner         |
         |            Guess A Number!           |
         |                 2023                 |        
         |                                      |
         #--------------------------------------#
      
       """)

playerName = input("Welcome to Guess A Number! What should I call you?\nPlease type your name into the space below and press ENTER.\n")
# Verify input whenever possible!
print(f"So, your name is {playerName}?")
isCorrect = input("Please verify if your input is correct. If it is, type yes. If it is not, type no.\n")
if isCorrect == "yes":
    print(f"Okay, {playerName}, shall we continue?")
else:
    playerName = input("What should I call you?\nPlease type your name into the space below and press ENTER.\n")



userDifficulty = (input("What would you like your difficulty setting to be? Easy, Normal, Hard, or Impossible?\nEasy mode = 6 guesses, 0 to 10 number range.\nNormal mode = 4 guesses, 0 to 15 number range.\nHard mode = 3 guesses, 0 to 20 number range.\nImpossible mode = 1 guess, 0 to 25 number range.\n"))
print(f"You have selected the user difficulty {userDifficulty}.\n")

if userDifficulty == "Easy":
    numAttempts = 6
    x = 0
    y = 10
elif userDifficulty == "Normal":
    numAttempts = 4
    x = 0
    y = 15
elif userDifficulty == "Hard":
    numAttempts = 3
    x = 0
    y = 20
elif userDifficulty == "Impossible":
    numAttempts = 1
    x = 0
    y = 25
else:
    print("No user input detected. Default difficulty has been set to Normal.\n")
    numAttempts = 4
    x = 0
    y = 15

userConfirm = (input("Do you wish to proceed? Type yes or no into the space below, then push ENTER\n"))
if userConfirm == "yes":
    print(f"Alright, {playerName}, now lets continue with our game.\n")
else:
    userDifficulty = (input("What would you like your difficulty setting to be? Easy, Normal, Hard, or Impossible?\n"))



# playerGuess
print(f"You need to guess a number between {x} to {y} to earn a point.\nIf you don't guess correctly, I get a point. You have {numAttempts} guesse(s).\n")

while playerScore != 3 and cpuScore != 3:
    #pass Tells Python to skip this block without giving an error message.
    secretNumber = random.randint(x, y) # Inclusive
    print(secretNumber)
    print(f"Player score: {playerScore}\nCPU score: {cpuScore}\n")
    numberOfGuesses = 0
    for guesses in range(numAttempts):
        print(f"You have {numAttempts - numberOfGuesses} guesses remaining in this round.\n")
        playerGuess = int(input("Think of a number, please type it in and then press ENTER.\n"))
        print(f"Alright, you have picked the number {playerGuess}. Lets see if this is a match!\n")
        if playerGuess == secretNumber:
            print("Congratulations! Its a match which means that you earn a point!\n")
            playerScore += 1
            winsound.PlaySound(loserSound, winsound.SND_FILENAME)
            break
        else:
            if playerGuess < secretNumber:
                print("Your guess is too low!\n")
            else:
                print("Your guess is too high!\n")
        numberOfGuesses += 1
    if playerGuess != secretNumber:
        print("Sorry, but I have won this round. I earn a point.\n")
        winsound.PlaySound(loserSound, winsound.SND_FILENAME)
        cpuScore += 1
        

if playerScore >= 3:
    print("You have won this game of Guess A Number! You can go about your day now.\n")
    imageWin.show('img/numberGuess/win.jpg')
else:
    print("The CPU has won this game of Guess A Number! You can go about your day now.\n")
    imageLoss.show('img/numberGuess/loser.jpg')

print("Memory Usage: (Current, Peak)")
print(tracemalloc.get_traced_memory)
tracemalloc.stop()