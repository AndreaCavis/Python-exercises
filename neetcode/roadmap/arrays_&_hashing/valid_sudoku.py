class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = len(board)
        for i in range(n):
            if not isLineValid(board[i]):
                return False
            
            column = []
            for j in range(n):
                if board[j][i] == ".":
                    continue
                column.append(board[j][i])

            if not isLineValid(column):
                return False
            
        return check_square(board)
    

def isLineValid(line: list[str]) -> bool:
    nums = []
    for value in line:
        if value == ".":
            continue
        nums.append(value)
    return True if len(nums) == len(set(nums)) else False


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
            # 012, 345, 678 are the indices for each line. row_group*3 aligns with the first square in each line (0,3,6). col_group does the same with columns.
            square_index = row_group * 3 + col_group
            squares[square_index].append(cell_value)

    # duplicate check
    for square in squares:
        if len(square) != len(set(square)):
            return False

    return True


board=[[".",".","4",".",".",".","6","3","."],
       [".",".",".",".",".",".",".",".","."],
       ["5",".",".",".",".",".",".","9","."],
       [".",".",".","5","6",".",".",".","."],
       ["4",".","3",".",".",".",".",".","1"],
       [".",".",".","7",".",".",".",".","."],
       [".",".",".","5",".",".",".",".","."],
       [".",".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".",".","."]]

print(Solution().isValidSudoku(board)) # False


'''
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Example 1:
Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: There are two 1's in the top-left 3x3 sub-box.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''