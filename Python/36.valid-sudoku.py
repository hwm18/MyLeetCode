#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
class Solution:
    # solution 2: Your runtime beats 93.03 % of python3 submissions
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board or len(board) == 0 or len(board[0]) == 0:
            return False

        return (self.is_row_valid(board) and
            self.is_col_valid(board) and
            self.is_square_valid(board))

    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True
        
    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True
        
    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)

    '''
    # solution 1: 
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board or len(board) == 0 or len(board[0]) == 0:
            return False

        # Method 1: compare the string
        result = set()
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                num = board[i][j]
                if num != ".":
                    row = str(num) + " row " + str(i)
                    col = str(num) + " column " + str(j)
                    sub = str(num) + " sub " + str(i // 3) + "-" + str(j // 3)
                    if row in result or col in result or sub in result:
                        return False
                    else:
                        result.add(row)
                        result.add(col)
                        result.add(sub)

        return True
    '''

