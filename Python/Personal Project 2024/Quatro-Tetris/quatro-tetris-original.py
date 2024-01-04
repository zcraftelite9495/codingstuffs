import pygame # Imports the Pygame Community Edition Modules

pygame.init() # Initializes the 'pygame' module

screen = pygame.display.set_mode((300,600)) # Sets the display width and hight using ((W,H))
pygame.display.set_caption("Quatro-Tetris: Original Tetris")

clock = pygame.time.Clock() # Sets the frame rate of the game (how fast the game will run), make sure to use capital C in 'Clock'
