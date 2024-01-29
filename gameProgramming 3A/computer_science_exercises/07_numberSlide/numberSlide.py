# Number Slide, Gavin Kloeckner, based on a project by Al Sweiggart, v0.4wip

# Game Setup / Steps
# Function to Layout / Setup the Grid
# Create the tiles and add them to the board
# Check for valid movements
# Animate movement of tile
# Allow for user input to select tile (mouse click)
# Identify location of coordinates of mouse click, determine tile selected
# Check for win -- All numbers in the correct order

# Divide and Conquer Method -- Break down a larger problem into smaller problems, then solve those problems

import pygame, sys, random
# sys module gives access to system level functions including open/close programse, etc.

from pygame.locals import *
# This line allows us to call functions directly instead of pygame.function()
# We can just write function()
# * in this line is a WILDCARD and means any or all
# Example: delete myGameFiles*

# Board Setup Data
# BOARDWIDTH = 4 # Columns
# BOARDHEIGHT = 4 # Rows

# # Tile Data
# TILESIZE = 80 # Measured in Pixels

# # Window Size
# WINDOWWIDTH = 640 # Measured in Pixels
# WINDOWHEIGHT = 480 # Measured in Pixels

# # Frams Per Second
# FPS = 30 # Sets maximum, does not "improve performance"

# # Blank Tile Value
# BLANK = None


# # Color Values = (R, G, B)
# # Minimum value = 0, maximum value = 255
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# BRIGHTBLUE = (0, 50, 255)
# DARKTURQUOISE = (3, 54, 73)
# GREEN = (0, 204, 0)

# # Assign colors to game objects
# BGCOLOR = DARKTURQUOISE
# TILECOLOR = GREEN
# TXTCOLOR = WHITE
# BORDERCOLOR = BRIGHTBLUE

# # Font Size
# BASICFONTSIZE = 20 # Measured in Pixels

# # Buttons and Messages
# BUTTONCOLOR = WHITE
# BUTTONTXTCOLOR = BLACK
# MESSAGECOLOR = WHITE

# # Margins for Windows
# XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH -1 ))) / 2)
# YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT -1 ))) / 2)

# # Directions
# UP = 'up'
# DOWN = 'down'
# LEFT = 'left'
# RIGHT = 'right'

# # Main Game Loop
# def main():
#     # global keyword makes Python use the same variable in the entire program
#     global FPSCLOCK, DISPLAYSURF, BASIC_FONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT
#     # SURF i9s the abbreviation for SURFACE
#     # A SURF in pygame can be used to draw graphics, text, or colors
#     # The easy way to think of the SURF is a whiteboard
    
#     # RECT is the abbreviation for RECTANGLE
    
#     # Start the pygame module itself. This line of code is required for it to work

#     pygame.init()

# def terminate() -> None:
#     pygame.quit()
#     sys.exit()

# def checkForQuit() -> None:
#     for event in pygame.event.get(QUIT):
#         terminate()
#     for event in pygame.event.get(KEYUP):
#         if event.key == K_ESCAPE:
#             terminate()
#         pygame.event.post(event)

# def getLeftTopOfTile(tileX: int, tileY: int) -> tuple:
#     left = XMARGIN + (tileX * TILESIZE) + (tileX - 1)
#     top = YMARGIN + (tileY * TILESIZE) + (tileY - 1)
#     return (top, left)

# def getSpotClick(board: List, x: int, y: int) -> tuple:
#     for tileX in range(len(board)):
#         for tileY in range(len(board[0])):
#             left, top = getLeftTopOfTile(tileX, tileY)
#             tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE)
#             if tileRect.collidepoint(x, y):
#                 return (tileX, tileY)
#     return (None, None)

