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

def displayBoard(incorrectLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(incorrectLetters)])
    print()

# i = 0            
# while i < 25:
#     getRandomWord(wordList)
#     i += 1
