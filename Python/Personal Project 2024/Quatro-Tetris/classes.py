import pygame # Ensures that the pygame tools are available for use in this classes file

class Colors: # Creates a class called 'Colors' which will store all the attributes for the colors needed in Quatro Tetris
    #Dark Grey
    dark_grey = (26, 31, 40)
    # Green
    green = (47, 230, 23)
    # Red
    red = (232, 18, 18)
    # Orange
    orange = (226, 116, 17)
    # Yellow
    yellow = (237, 234, 4)
    # Purple
    purple = (166, 0, 247)
    # Cyan
    cyan = (21, 204, 209)
    # Blue
    blue = (13, 64, 216)

    @classmethod
    def get_cell_colors(cls): # Defines the command that defines colors and their index values

        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]

class gridOriginal: # Creates a class called 'gridOriginal'
    def __init__(self): # Creates a list of actions to be executed when the class (gridOriginal) is imported
        self.num_rows = 20 # Defines the number of rows 
        self.num_cols = 10 # Defines the number of columns
        self.cell_size = 30 # Defines the size of the cells in pixels
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] 
        # The above defines an array of Zeros, a list of lists basically. Each list will have 1 zero for each column and the amount of lists is equal to the amount of rows. Instead of making the list ourselves, which would take up a bery substanstial amount of space, we use a 'for' command to automate the placement of the zeros. The first part of the command prints a zero for every number of columns and the second repeats the first command for the number of rows.
        self.colors = Colors.get_cell_colors()

    def print_grid(self): # Defines the command that prints the grid
        for row in range(self.num_rows): # Completes the following action for every row
            for column in range(self.num_cols): # Completes the following action for every column
                print(self.grid[row][column], end = " ") # Prints the values for the array into the terminal window
            print ()

    def is_inside(self, row, column): # Defines the command that checks if the block has gone past the boundries of the grid
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    def draw(self, screen): # Defines the command that draws the cells on the screen
        # To get the values of all the numbers in the array, we use a nested loop
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size +1, self.cell_size -1, self.cell_size -1) # Creates the grid's cells, by multiplying the columns and rows by the cell_size and setting the cell size to cell_size.
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect) # Draws the rectange(s) on the screen according to the following values

class Position: # Creates a class called 'Position' which will be used to help represent a position in a two-dimensional grid using a single object
    def __init__(self, row, column): # Creates a list of actions to be executed when the class (Position) is imported
        self.row = row
        self.column = column

class Block: # Creates a class called 'Block' which will be the parent class for all the tetris blocks
    def __init__(self, id): # Creates a list of actions to be executed when the class (Block) is imported
        self.id = id # Initializes the 'id' variable
        self.cells = {} # Initializes the 'cells' variable
        self.cell_size = 30 # Sets the Cell Size
        self.row_offset = 0 # Sets the row offset of the block
        self.column_offset = 0 # Sets the column offset of the block
        self.rotation_state = 0 # Initializes the Rotation State
        self.Colors = Colors.get_cell_colors() 

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            print("Ran once")
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles


    def draw(self, screen): # Creates a command that draws the current block
        tiles = self.get_cell_positions() # Sets the tile variable to the rotation state and cells of the block
        for tile in tiles: 
            tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1) # Sets the paramaters for the rect
            pygame.draw.rect(screen, self.Colors[self.id], tile_rect) # Draws the rect