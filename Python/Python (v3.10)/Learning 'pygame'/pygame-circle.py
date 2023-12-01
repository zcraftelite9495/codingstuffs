# Import the modules used in the code
import pygame

# Initializes the pygame library, used in this code for displaying graphics on the game screen
pygame.init()

# Sets up the game's window size and draw area
screen = pygame.display.set_mode([500,500])

# Script that makes sure the game runs until the user quits the game
running = True
while running:

    # Detects if the user closes the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fills the screen backround with black
    screen.fill((0, 0, 0))

    # This will draw a circle in the center of the screen
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flips the display so it displays correctly
    pygame.display.flip()

# Quits the game
pygame.quit()