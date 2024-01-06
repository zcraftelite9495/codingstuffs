import pygame # Ensures that the pygame tools are available for use in this classes file

class gridOriginal: # Creates a class called 'Grid_Original'
    def __init__(self): # Creates a list of actions to be executed when the class (gridOriginal) is imported
        self.num_rows = 20 # Defines the number of rows
        self.num_cols = 10 # Defines the number of columns
        self.cell_size = 30 # Defines the size of the cells in pixels
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] 
        # The above defines an array of Zeros, a list of lists basically. Each list will have 1 zero for each column and the amount of lists is equal to the amount of rows. Instead of making the list ourselves, which would take up a bery substanstial amount of space, we use a 'for' command to automate the placement of the zeros. The first part of the command prints a zero for every number of columns and the second repeats the first command for the number of rows.
        self.colors = self.get_cell_colors()

    def print_grid(self): # Defines the command that prints the grid
        for row in range(self.num_rows): # Completes the following action for every row
            for column in range(self.num_cols): # Completes the following action for every column
                print(self.grid[row][column], end = " ") # Prints the values for the array into the terminal window
            print ()

    def get_cell_colors(self): # Defines the command the defines colors and their index values
        
        # Dark Grey
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

        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]

    def draw(self, screen): # Defines the command that draws the cells on the screen
        # To get the values of all the numbers in the array, we use a nested loop
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size, row*self.cell_size, self.cell_size, self.cell_size) # Creates the grid's cells, by multiplying the columns and rows by the cell_size and setting the cell size to cell_size.
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect) # Draws the rectange(s) on the screen according to the following values

