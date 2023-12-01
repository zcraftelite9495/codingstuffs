# Quatro Tetris (gametest) v0.0.1

# Import the modules used in the code
import pygame

# Import pygame.locals to easily access key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Sets the screen Width & Height
SCREEN_WIDTH=600
SCREEN_HEIGHT=800

# Initializes the pygame library, used in this code for displaying graphics on the game screen
pygame.init()

# Sets up the game's window size and draw area
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Script that makes sure the game runs until the user quits the game
running = True
while running:

    for event in pygame.event.get():
        #  Detects and quits if the user closes the window
        if event.type == pygame.QUIT:
            running = False

        # Detects and quits if the user hits the escape key
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    # Fills the screen backround with black
    screen.fill((0, 0, 0))

    # Create a surface and defines its length and width
    surf = pygame.surface((50, 50))

    # Gives the surface a color to sepeerate it from the backround
    surf.fill((255, 255, 255))
    rect = surf.get_rect()

# Quits the game
pygame.quit()