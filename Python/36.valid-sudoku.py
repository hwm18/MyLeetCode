#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
class Solution:
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

