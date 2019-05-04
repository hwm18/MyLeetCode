#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return

        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

