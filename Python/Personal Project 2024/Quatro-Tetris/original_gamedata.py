import pygame # Ensures that the pygame tools are available for use in this classes file
import random # Ensures that the random tools are available for use in this classes file

from blockClasses import * # Makes sure the block classes are available within this file
from classes import Block # Makes sure the Block class is available within this file

class Game: # Creates a class called 'Game' which will store all the attributes and modules to control the safe runtime of the game
    def __init__(self):
        self.grid = gridOriginal() # Sets 'gridOriginal' to 'grid'
        self.blocks = [I_Block(), J_Block(), L_Block(), O_Block(), S_Block(), T_Block(), Z_Block()] # Defines all the tetrominos
        self.current_block = self.get_random_block() # Gets a random block to show
        self.next_block = self.get_random_block() # Gets a random block to show next

    def get_random_block(self):
        if len(self.blocks) == 0: # Refills the blocks list when it is empty
            self.blocks = [I_Block(), J_Block(), L_Block(), O_Block(), S_Block(), T_Block(), Z_Block()]
        block = random.choice(self.blocks) # Gets a random block
        self.blocks.remove(block) # Removes the chosen block
        return block # Returns the 'block' value

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)