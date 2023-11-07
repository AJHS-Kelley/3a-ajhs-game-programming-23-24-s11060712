import random
wordList = 'cat fish dog car hippo tail red blue green cyan make break tall small real meal krill teal cow moose'.split()
# .split() will split a string into separate elements, by default based on SPACE

# VARIABLE_NAMES that are all caps are constants and not meant to change
HANGMAN_BOARD = ['''
    +-----+
          |  
          |   
          |   
          |   
        =====''', '''     
    +-----+
    O     |  
          |   
          |   
          |   
        =====''', '''             
    +-----+
    O     |  
    |     |   
          |   
          |   
        =====''', '''         
    +-----+
    O     |  
    |\    |   
          |   
          |   
        =====''', '''         
    +-----+
    O     |  
   /|\    |   
          |   
          |   
        =====''', '''             
    +-----+
    O     |  
   /|\    |   
   /      |   
          |   
        =====''', '''             
    +-----+
    O     |  
   /|\    |   
   / \    |   
          |   
        =====''']                                           

def getRandomWord(wordList):
    wordIndex = random.randint(0 , len(wordList) - 1)
    # len(listName) - 1 is the most common way to prevent index out of range
    print(wordIndex)
    print(wordList[wordIndex])
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    # Display any incorrect guesses

    print('Missed Letters:', end = ' ')
    for letters in missedLetters:
        print(letters, end = ' ')
    print()

    blanks = '_' * len(secretWord)
    
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
            # The : character is used to slice strings into pieces.
            # [:i] means slice from the start until index i
            # [i+1:] means slice from the i+1 until the end
            # [startingPoint:endingPoint]
            
    for letters in blanks:
        print(letters, end = '')
    print()

def getGuess(alreadyGuessed):
    # Only allow: single character, A-Z only, not guessed already
    while True: # Default infinite loop
        print('Please guess a letter and press enter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please put a single letter.\n')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter an English letter only.')
        elif guess in alreadyGuessed:
            print('What you put has already been guessed. Please guess a different letter.\n')
        else:
            return guess
        
def playAgain():
    print('Would you like to play again?\nPlease type YES or NO in the space below\n')
    return input().upper().startswith('y') # return True/False based on input

# Start The Game
print('Welcome to Hangman! Shall we get started?\n') # A backslash (\) escapes special characters
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(wordList)
print('The secret word is ' + secretWord)
gameIsDone = False

# Game Loop begins here
while True: # 99% of the time, the loop will start this way
    # Two ways to exit while True: return OR break
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)
    
    if guess in secretWord: # Is the guess in the secretWord?
        correctLetters = correctLetters + guess

        # Check for victory
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('We have ourselves a winner!\nThank you for playing!\n')
            gameIsDone = True
    else: # Missed letter
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_BOARD) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Sorry, but you lost the game. You guessed too many times\n')
            print('The secret word was: ' + secretWord)
            gameIsDone = True
    

# i = 0            
# while i < 25:
#     getRandomWord(wordList)
#     i += 1
