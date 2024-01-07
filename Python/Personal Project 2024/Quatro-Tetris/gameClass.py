import pygame # Ensures that the pygame tools are available for use in this classes file
import random # Ensures that the random tools are available for use in this classes file

from blockClasses import * # Makes sure the block classes are available within this file
from classes import Block # Makes sure the Block class is available within this file
from classes import gridOriginal # Makes sure the Grid class is available within this file

class Game: # Creates a class called 'Game' which will store all the attributes and modules to control the safe runtime of the game
    def __init__(self): # Initializes the 'Game' class
        self.grid = gridOriginal() # Sets 'gridOriginal' to 'grid'
        self.blocks = [I_Block(), J_Block(), L_Block(), O_Block(), S_Block(), T_Block(), Z_Block()] # Defines all the tetrominos
        self.current_block = self.get_random_block() # Gets a random block to show
        self.next_block = self.get_random_block() # Gets a random block to show next

    def get_random_block(self): # Defines the command to get a random block
        if len(self.blocks) == 0: # Refills the blocks list when it is empty
            self.blocks = [I_Block(), J_Block(), L_Block(), O_Block(), S_Block(), T_Block(), Z_Block()]
        block = random.choice(self.blocks) # Gets a random block
        self.blocks.remove(block) # Removes the chosen block
        return block # Returns the 'block' value

    def move_left(self): # Defines the command to move the block left
        self.current_block.move(0, -1)
        if self.block_inside() == False:
            self.current_block.move(0, 1)

    def move_right(self): # Defines the command to move the block right
        self.current_block.move(0, 1)
        if self.block_inside() == False:
            self.current_block.move(0, -1)

    def move_down(self): # Defines the command to move the block down (faster)
        self.current_block.move(1, 0)
        if self.block_inside() == False:
            self.current_block.move(-1, 0)

    def block_inside(self): # Defines the command to check for boundries
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            print(tile.row)
            print(tile.column)
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False 
        return True

    def draw(self, screen): # Defines the command to draw updates on the screen
        self.grid.draw(screen)
        self.current_block.draw(screen)