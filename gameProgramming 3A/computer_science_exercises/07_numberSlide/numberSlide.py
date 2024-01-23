# Number Slide, Gavin Kloeckner, based on a project by Al Sweiggart, v0.2

# Game Setup / Steps
# Function to Layout / Setup the Grid
# Create the tiles and add them to the board
# Check for valid movements
# Animate movement of tile
# Allow for user input to select tile (mouse click)
# Identify location of coordinates of mouse click, determine tile selected
# Check for win -- All numbers in the correct order

# Divide and Conquer Method -- Break down a larger problem into smaller problems, then solve those problems

# Board Setup Data
BOARDWIDTH = 4 # Columns
BOARDHEIGHT = 4 # Rows

# Tile Data
TILESIZE = 80 # Measured in Pixels

# Window Size
WINDOWWIDTH = 640 # Measured in Pixels
WINDOWSIZE = 480 # Measured in Pixels

# Frams Per Second
FPS = 30 # Sets maximum, does not "improve performance"

# Blank Tile Value
BLANK = None


# Color Values = (R, G, B)
# Minimum value = 0, maximum value = 255
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQUOISE = (3, 54, 73)
GREEN = (0, 204, 0)

# Assign colors to game objects
BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE

# Font Size
BASICFONTSIZE = 20 # Measured in Pixels