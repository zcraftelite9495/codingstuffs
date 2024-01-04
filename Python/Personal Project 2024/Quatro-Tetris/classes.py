class gridOriginal # Creates a class called 'Grid_Original'
    def __init__(self): # Creates a list of actions to be executed when the class (gridOriginal) is imported
        self.num_rows = 20 # Defines the number of rows
        self.num_cols = 10 # Defines the number of columns
        self.cell_size = 30 # Defines the size of the cells in pixels
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] 
        # The above defines an array of Zeros, a list of lists basically. Each list will have 1 zero for each column and the amount of lists is equal to the amount of rows. Instead of making the list ourselves, which would take up a bery substanstial amount of space, we use a 'for' command to automate the placement of the zeros. The first part of the command prints a zero for every number of columns and the second repeats the first command for the number of rows.

    def print_grid(self): # Defines the command that prints the grid
        for row in range(self.num_rows): # Completes the following action for every row
            for column in range(self.num_cols): # Completes the following action for every column
                print(self.grid[row][column], end = " ")
            print ()