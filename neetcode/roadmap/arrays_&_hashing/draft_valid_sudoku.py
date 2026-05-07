# function to navigate the sudoku grid

def check_square(board: list[list[str]]) -> list[list[str]]:
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
            # 012, 345, 678 are the indices for each line. row_group*3 aligns with the first square in each line (0,3,6). col_group does the same with columns.
            square_index = row_group * 3 + col_group
            squares[square_index].append(cell_value)

    return squares




board = [["1","2",".",".","3",".",".",".","."],
         ["4",".",".","5",".",".",".",".","."],
         [".","9","8",".",".",".",".",".","3"],
         ["5",".",".",".","6",".",".",".","4"],
         [".",".",".","8",".","3",".",".","5"],
         ["7",".",".",".","2",".",".",".","6"],
         [".",".",".",".",".",".","2",".","."],
         [".",".",".","4","1","9",".",".","8"],
         [".",".",".",".","8",".",".","7","9"]]

print(check_square(board))