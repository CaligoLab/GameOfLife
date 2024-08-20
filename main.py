import matplotlib.pyplot as plt
class GameOfLife(object):
    '''
    A class to represent Conway's Game of Life.
    The Game of Life is a cellular automaton devised by mathematician John Conway.
        This class allows you to simulate the game on a grid of arbitrary size.
    The grid is presented in the following way: dead cells are black, live cells are orange.
    '''

    def __init__(self, x_dim, y_dim):
        '''
        Initializes the game grid with the specified dimensions as a 2D array
            Parameters:
        x_dim: An integer representing the number of rows in the grid.
        y_dim: An integer representing the number of columns in the grid.
            Returns:
        None
        '''

        self.x_dim = x_dim
        self.y_dim = y_dim
        self.grid = [[0 for _ in range(y_dim)] for _ in range(x_dim)]

    def get_grid(self):
        '''
        Returns the current state of the game grid
            Parameters:
        None
            Returns:
        A 2D list representing the game grid, where 1 indicates a live cell and 0 indicates a dead cell
        '''

        return self.grid

    def print_grid(self):
        '''
       Prints the current state of the game grid in as an array of 1s and 0s with horizontal and vertical dividers
           Parameters:
       None
           Returns:
       None
       '''

        for row in self.grid:
            print("|".join(str(element) for element in row))
        # Horizontal divider
            print("-" * (self.y_dim * 2))

    def populate_grid(self, coord):
        '''
        Populates the game grid with live cells at the specified coordinates
            Parameters:
        coord: A list of tuples. Each tuple represents the (x, y) coordinates of a live cell
            Returns:
        None
        '''

        for (row, col) in coord:
            if 0 <= row < self.x_dim and 0 <= col < self.y_dim:
                self.grid[row][col] = 1
            else:
                print(f"Warning: Coordinates ({row}, {col}) are out of bounds.")

    def count_live_neighbors(self, row, col):
        # Additional method not to overload the make_step() method
        '''
        Counts the number of live neighbors for a cell at a given position.
            Parameters:
        row: An integer representing the row index of the cell.
        col: An integer representing the column index of the cell.
            Returns:
        An integer representing the number of live neighbors.
        '''

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        live_neighbors = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.x_dim and 0 <= c < self.y_dim:
                live_neighbors += self.grid[r][c]
        return live_neighbors

    def make_step(self):
        '''
         Advances the game by one step according to the rules of Conway's Game of Life.
         This method updates the game grid based on the current state,
         applying the rules to determine the next state of each cell.
             Parameters:
         None
             Returns:
         None
         '''

        # Create an interim grid to store the next state
        interim_grid = [[0 for _ in range(self.y_dim)] for _ in range(self.x_dim)]

        # Iterate over each cell in the grid
        for row in range(self.x_dim):
            for col in range(self.y_dim):
                live_neighbors = self.count_live_neighbors(row, col)

                # Apply the Game of Life rules
                # Cell is alive:
                if self.grid[row][col] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        interim_grid[row][col] = 0  # Cell dies
                    else:
                        interim_grid[row][col] = 1  # Cell lives
                # Cell is dead:
                else:
                    if live_neighbors == 3:
                        interim_grid[row][col] = 1  # Cell becomes alive

        # Update the grid to the new state
        self.grid = interim_grid

    def make_n_steps(self, n):
        '''
       Advances the game by a specified number of steps.
       This method repeatedly applies the make_step method to evolve the game state over n steps.
           Parameters:
       n: An integer representing the number of steps to advance the game.
           Returns:
       None
       '''

        # Apply the make_step method n times
        for _ in range(n):
            self.make_step()

    def draw_grid(self):
        '''
         Creates a scatter plot of the current grid state.
         Live cells are shown as orange squares, and dead cells are not plotted,
         but are implied as black (the color of the background)
             Parameters:
         None
             Returns:
         None
         '''

        live_cells_x = []
        live_cells_y = []

        # Iterate over the grid to create lists of coords for live cells
        for row in range(self.x_dim):
            for col in range(self.y_dim):
                if self.grid[row][col] == 1:
                    live_cells_x.append(col)  # x-coordinate (column index)
                    live_cells_y.append(row)  # y-coordinate (row index)

        # Create a scatter plot
        plt.figure(figsize=(10, 10))
        plt.scatter(live_cells_x, live_cells_y, color='orange', marker='s', s=100)
        # Invert y-axis to match the printed grid orientation
        plt.gca().invert_yaxis()
        # for harmonious presentation
        plt.xlim(-0.5, self.y_dim - 0.5)
        plt.ylim(-0.5, self.x_dim - 0.5)
        plt.gca().set_facecolor('black')
        plt.grid(True, color="gray")
        plt.show()

    def run_until_stable(self, max_steps=1000):
        '''
        Runs the Game of Life until the pattern stops changing or until a maximum number of steps is reached
            Parameters:
        max_steps: An optional integer specifying the maximum number of steps to simulate (default is 1000).
            Returns:
        The number of steps taken to reach a stable state.
        '''

        previous_grid = None
        steps = 0

        while steps < max_steps:
            # Save the current grid state to compare later
            previous_grid = [row[:] for row in self.grid]  # Create a deep copy of the grid

            # Make one step
            self.make_step()

            # Increment the step count
            steps += 1

            # Check if the grid has stabilized (i.e., no changes from the previous step)
            if self.grid == previous_grid:
                print(f"Pattern stabilized after {steps} steps.")
                break
        else:
            print(f"Reached maximum of {max_steps} steps without stabilizing.")

        return steps

    def run_until_all_dead(self, max_steps=1000):
        '''
        Runs the Game of Life until all living cells die or a maximum number of steps is reached
            Parameters:
        max_steps: An optional integer specifying the maximum number of steps to simulate (default is 1000).
            Returns:
        The number of steps taken until all cells are dead. If max_steps is reached without all cells dying,
        it returns max_steps.
        '''

        steps = 0

        while steps < max_steps:
            # Check if all cells are dead
            if not any(1 in row for row in self.grid):
                print(f"All cells are dead after {steps} steps.")
                break

            # Make one step
            self.make_step()

            # Increment the step count
            steps += 1
        else:
            print(f"Reached maximum of {max_steps} steps without all cells dying.")

        return steps

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    GameOfLife(3, 5)