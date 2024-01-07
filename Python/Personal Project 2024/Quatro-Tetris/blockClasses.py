import pygame # Ensures that the pygame tools are available for use in this classes file
from classes import Block # Ensures the Block class is available for use in this file
from classes import Position # Ensure the Position class is available for use in this file

class L_Block(Block): # Creates a class for the L Tetromino
    def __init__(self): 
        super().__init__(id = 1) # Initializes the parent class' data
        self.cells = { # Defines rotation states' cell positions
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            # [-][-][1]
            # [1][1][1]
            # [-][-][-]
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            # [-][1][-]
            # [-][1][-]
            # [-][1][1]
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            # [-][-][-]
            # [1][1][1]
            # [1][-][-]
            3: [Position(0 ,0), Position(0, 1), Position(1, 1), Position(2, 1)]
            # [1][1][-]
            # [-][1][-]
            # [-][1][-]
        }
        self.move(0, 3)

class J_Block(Block): # Creates a class for the J Tetromino
    def __init__(self):
        super().__init__(id = 2) # Initializes the parent class' data
        self.cells = { # Defines rotation states' cell positions
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            # [2][-][-]
            # [2][2][2]
            # [-][-][-]
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            # [-][2][2]
            # [-][2][-]
            # [-][2][-]
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            # [-][-][-]
            # [2][2][2]
            # [2][-][-]
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
            # [-][2][-]
            # [-][2][-]
            # [2][2][-]
        }
        self.move(0, 3)

class I_Block(Block): # Creates a class for the I Tetromino
    def __init__(self):
        super().__init__(id = 3) # Initializes the parent class' data
        self.cells = { # Defines rotation states' cell positions
            0: [Position(1, 0), Position(1, 2), Position(1, 3), Position(1, 4)],
            # [-][-][-][-]
            # [3][3][3][3]
            # [-][-][-][-]
            # [-][-][-][-]
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            # [-][-][3][-]
            # [-][-][3][-]
            # [-][-][3][-]
            # [-][-][3][-]
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            # [-][-][-][-]
            # [-][-][-][-]
            # [3][3][3][3]
            # [-][-][-][-]
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
            # [-][3][-][-]
            # [-][3][-][-]
            # [-][3][-][-]
            # [-][3][-][-]
        }
        self.move(0, 3)

class O_Block(Block): # Creates a class for the O Tetromino
    def __init__(self):
        super().__init__(id = 4)
        self.cells = { # Defines rotation states' cell positions
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            # [4][4]
            # [4][4]
            1: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            # [4][4]
            # [4][4]
            2: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            # [4][4]
            # [4][4]
            3: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
            # [4][4]
            # [4][4]
        }
        self.move(0, 4)

class S_Block(Block): # Creates a class for the S Tetromino
    def __init__(self):
        super().__init__(id = 5)
        self.cells = { # Defines rotation states' cell positions
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            # [-][5][5]
            # [5][5][-]
            # [-][-][-]
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            # [-][5][-]
            # [-][5][5]
            # [-][-][5]
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            # [-][-][-]
            # [-][5][5]
            # [5][5][-]
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
            # [5][-][-]
            # [5][5][-]
            # [-][5][-]
        }
        self.move(0, 3)

class T_Block(Block): # Creates a class for the T Tetromino
    def __init__(self):
        super().__init__(id = 6)
        self.cells = { # Defines rotation states' cell positions
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            # [-][6][-]
            # [6][6][6]
            # [-][-][-]
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            # [-][6][-]
            # [-][6][6]
            # [-][6][-]
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            # [-][-][-]
            # [6][6][6]
            # [-][6][-]
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
            # [-][6][-]
            # [6][6][-]
            # [-][6][-]
        }
        self.move(0, 3)

class Z_Block(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = { # Defines rotation states' cell positions
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            # [7][7][-]
            # [-][7][7]
            # [-][-][-]
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            # [-][-][7]
            # [-][7][7]
            # [-][7][-]
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            # [-][-][-]
            # [7][7][-]
            # [-][7][7]
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
            # [-][7][-]
            # [7][7][-]
            # [7][-][-]
        }
        self.move(0, 3)