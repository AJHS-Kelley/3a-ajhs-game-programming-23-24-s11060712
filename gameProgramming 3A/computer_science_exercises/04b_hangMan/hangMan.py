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
    pass

# i = 0            
# while i < len(HANGMAN_BOARD):
#     print(HANGMAN_BOARD[i])
#     i += 1
