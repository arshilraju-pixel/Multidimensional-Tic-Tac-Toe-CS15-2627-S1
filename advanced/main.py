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

grid = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

current_player = "X"

print("Welcome to Arshia's Multidimensional Tic-Tac-Toe Game!")
print("Enter row and column numbers from 0 to 2.")
print()

display_grid(grid)

while determine_winner(grid) == "No winner yet":

    print(f" It's Player {current_player}'s turn!")

    try:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid position! Row and column must be between 0 and 2.")
        continue

    if grid[row][col] != "-":
        print("That space is already taken.")
        continue


    grid[row][col] = current_player


    print()
    display_grid(grid)

    result = determine_winner(grid)

    if result == "X" or result == "O":
        print(f"Player {result} wins!")
        break

    elif result == "Tie":
        print("Tie!")
        break


    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"