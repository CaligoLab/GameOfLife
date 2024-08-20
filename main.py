import matplotlib.pyplot as plt
class GameOfLife(object):

    def __init__(self, x_dim, y_dim):
        # Initialize a 2D list with dimensions x_dim by y_dim filled with zeros.
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.grid = [[0 for _ in range(y_dim)] for _ in range(x_dim)]

    def get_grid(self):
        # Implement a getter method for your grid.
        return self.grid

    def print_grid(self):
        # Implement a method to print out your grid in a human-readable format.
        for row in self.grid:
            print("|".join(str(element) for element in row))
        # Horizontal divider
            print("-" * (self.y_dim * 2))

    def populate_grid(self, coord):
        # Given a list of 2D coordinates (represented as tuples/lists with 2 elements each),
        # set the corresponding elements in your grid to 1.
        for (row, col) in coord:
            if 0 <= row < self.x_dim and 0 <= col < self.y_dim:
                self.grid[row][col] = 1
            else:
                print(f"Warning: Coordinates ({row}, {col}) are out of bounds.")

    def count_live_neighbors(self, row, col):
        # Additional method not to overload the make_step() method
        # Count the live neighbors of a cell at position (row, col).
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        live_neighbors = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.x_dim and 0 <= c < self.y_dim:
                live_neighbors += self.grid[r][c]
        return live_neighbors

    def make_step(self):
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
        # Apply the make_step method n times
        for _ in range(n):
            self.make_step()

    def draw_grid(self):
        ''' Create a scatter plot of the current grid state '''

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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    GameOfLife(3, 5)