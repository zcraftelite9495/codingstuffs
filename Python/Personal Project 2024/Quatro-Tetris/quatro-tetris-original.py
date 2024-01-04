import pygame # Imports the Pygame Community Edition Modules
import sys # Imports the Python Internal System Extension Modules

pygame.init() # Initializes the 'pygame' module

# Initializing display window
screen = pygame.display.set_mode((300,600)) # Sets the display width and hight using ((W,H))
pygame.display.set_caption("Quatro-Tetris: Original Tetris") # Sets the game's window title

# Initializing shortcuts to commands
clock = pygame.time.Clock() 

# Initializng Colors
dark_blue = (44, 44, 127) # Dark Blue

while True: # Initiates the main game loop
    # Checking for Events
    ## Checks for events to stop the game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Detects if the 'x' button is pressed, and runs the following commands
            pygame.quit() # Closes the game
            sys.exit() # Exits the python interpreter
    
    # Drawing objects
    screen.fill(dark_blue)
    pygame.display.update() # Updates all objects on the screen 
    clock.tick(60) # Sets the framerate of the game, to keep it running consistently

    # Updating position of objects

    # Drawing new position of objects
    