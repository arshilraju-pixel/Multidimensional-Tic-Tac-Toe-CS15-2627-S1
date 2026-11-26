grid_1 = [
    ["X", "X", "X"],
    ["O", "O", "X"],
    ["O", "X", "O"]
]

grid_2 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "O", "X"]
]

grid_3 = [
    ["X", "O", "O"],
    ["O", "X", "X"],
    ["O", "X", "X"]
]

grid_4 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "X", "X"]
]

def display_grid(grid):
    for row in range(3):
        print(" " + " | ".join(grid[row]))

        if row < 2:
            print("---+---+---")


def determine_winner(grid):


    for row in range(3):
        if grid[row][0] == grid[row][1] == grid[row][2] and grid[row][0] != "-":
            return grid[row][0]


    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != "-":
            return grid[0][col]


    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != "-":
        return grid[0][0]


    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != "-":
        return grid[0][2]


    for row in range(3):
        for col in range(3):
            if grid[row][col] == "-":
                return "No winner yet"

    return "Tie"


boards = [grid1, grid2, grid3, grid4]

for i, grid in enumerate(boards, start=1):

    print(f"Board {i}:")
    display_grid(grid)

    result = determine_winner(grid)

    if result == "X" or result == "O":
        print(f"Winner: {result}!")
    elif result == "Tie":
        print("Game ended in a tie!")
    else:
        print("No winner yet.")