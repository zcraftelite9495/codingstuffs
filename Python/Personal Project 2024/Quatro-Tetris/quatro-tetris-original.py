# v0.0.1a-43
splashFile = open('splash-original.txt', 'r')
splash = splashFile.read()
print(splash)
splashFile.close()
print('Anything shown in this terminal is either used for debugging purposes, or non display purposes, please diregard anything displayed in this terminal screen.') # Shows warning to end user about outputs to the Terminal Screen
import pygame # Imports the Pygame Community Edition Modules
import sys # Imports the Python Internal System Extension Modules

from classes import gridOriginal # Imports the 'gridOriginal' Class from the classes.py file we made earlier
from classes import Colors # Imports the 'Colors' Class from the classes.py file we made earlier
from blockClasses import * # Imports all the blocks from the blockClasses.py file we emade earlier

pygame.init() # Initializes the 'pygame' module

# Initializing display window
screen = pygame.display.set_mode((300,600)) # Sets the display width and hight using ((W,H))
pygame.display.set_caption("Quatro-Tetris: Original Tetris") # Sets the game's window title

# Initializing shortcuts to commands
clock = pygame.time.Clock()
gameGrid = gridOriginal()

# Initializng Backround Color
dark_blue = (44, 44, 127) # Dark Blue

# Testing the display of a tetrimino
block = T_Block()
block.move(4, 3)


while True: # Initiates the main game loop
    # Checking for Events
    ## Checks for events to stop the game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Detects if the 'x' button is pressed, and runs the following commands
            pygame.quit() # Closes the game
            sys.exit() # Exits the python interpreter
    
    # Drawing objects
    screen.fill(dark_blue) # Fills the backround of the screen with Dark Blue
    gameGrid.draw(screen) # Draws the game grid on the screen
    block.draw(screen) # Testing the display of a tetrimino
    pygame.display.update() # Updates all objects on the screen 
    clock.tick(60) # Sets the framerate of the game, to keep it running consistently

    # Updating position of objects

    # Drawing new position of objects
    