# v0.0.1a-69
splashFile = open('splash-original.txt', 'r')
splash = splashFile.read()
print(splash)
splashFile.close()
print('Anything shown in this terminal is either used for debugging purposes, or non display purposes, please diregard anything displayed in this terminal screen.') # Shows warning to end user about outputs to the Terminal Screen
import pygame # Imports the Pygame Community Edition Modules
import sys # Imports the Python Internal System Extension Modules
import random # Improts the Randomized Extension Modules

from classes import Colors # Imports the 'Colors' Class from the classes.py file we made earlier
from blockClasses import * # Imports all the blocks from the blockClasses.py file we emade earlier
from gameClass import Game # Imports the 'Game' Class from the classes.py file we made earlier

pygame.init() # Initializes the 'pygame' module

# Initializing display window
screen = pygame.display.set_mode((300,600)) # Sets the display width and hight using ((W,H))
pygame.display.set_caption("Quatro-Tetris: Original Tetris") # Sets the game's window title

# Initializing shortcuts to commands
clock = pygame.time.Clock()
game = Game()

# Initializng Backround Color
dark_blue = (44, 44, 127) # Dark Blue

while True: # Initiates the main game loop
    # Checking for Events
    ## Checks for events to stop the game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Detects if the 'x' button is pressed, and runs the following commands
            pygame.quit() # Closes the game
            sys.exit() # Exits the python interpreter

        if event.type == pygame.KEYDOWN: # Detects if a key is pressed
            if event.key == pygame.K_LEFT: # Detects if that key is the "←" key
                game.move_left()

            if event.key == pygame.K_RIGHT: # Detects if that key is the "→" key
                game.move_right()

            if event.key == pygame.K_DOWN: # Detects if that key is the "↓" key
                game.move_down()

    
    # Drawing objects
    screen.fill(dark_blue) # Fills the backround of the screen with Dark Blue
    game.draw(screen) # Draws the game on the screen
    pygame.display.update() # Updates all objects on the screen 
    clock.tick(60) # Sets the framerate of the game, to keep it running consistently

    # Updating position of objects

    # Drawing new position of objects
    