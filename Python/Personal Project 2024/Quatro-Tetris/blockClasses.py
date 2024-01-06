import pygame # Ensures that the pygame tools are available for use in this classes file
from classes import Block # Ensures the Block class is available for use in this file
from classes import Position # Ensure the Position class is available for use in this file

class L_Block(Block): # Creates a class for the L Tertromino
    def __init__(self): 
        super().__init__(id = 1) # Initializes the parent class' data
        id = 1 # Sets the ID of the file
        self.cells = { # Defines rotation states' cell positions
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            # [0][0][1]
            # [1][1][1]
            # [0][0][0]
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            # [0][1][0]
            # [0][1][0]
            # [0][1][1]
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            # [0][0][0]
            # [1][1][1]
            # [1][0][0]
            3: [Position(0 ,0), Position(0, 1), Position(1, 1), Position(2, 1)]
            # [1][1][0]
            # [0][1][0]
            # [0][1][0]
        }