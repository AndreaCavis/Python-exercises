# function to navigate the sudoku grid

def check_square(board: list[list[str]]) -> bool:
    # create the 9 bucket squares for 3x3 squares numbers
    squares = [[] for _ in range(9)]

    for row_index, row in enumerate(board):
        # diving by 3 a 9 grid makes sure each row belongs to the associated square (0//3=0, 1//3=0, 4//3=1, etc...)
        row_group = row_index // 3

        # navigate through the row to get all columns
        for col_index, cell_value in enumerate(row):
            # immediate check to avoid wasting time
            if cell_value == ".":
                continue

            col_group = col_index // 3


    return True




board = [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","1",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]

check_square(board)