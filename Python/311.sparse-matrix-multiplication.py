#
# @lc app=leetcode id=311 lang=python
#
# [311] Sparse Matrix Multiplicaiton
#
# https://www.lintcode.com/problem/sparse-matrix-multiplication/description
#
# Given two Sparse Matrix A and B, return the result of AB.
# You may assume that A's column number is equal to B's row number.
# Example1
# Input: 
# [[1,0,0],[-1,0,3]]
# [[7,0,0],[0,0,0],[0,0,1]]
# Output:
# [[7,0,0],[-7,0,3]]
# Explanation:
# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]

# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]

#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |
# Example2

# Input:
# [[1,0],[0,1]]
# [[0,1],[1,0]]
# Output:
# [[0,1],[1,0]]
# 
#
class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        n,m,k = len(A),len(A[0]),len(B[0])
        result = [[0] * k for i in range(n)]
        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    continue
                
                for l in range(k):
                    result[i][l] +=  A[i][j] * B[j][l]
                
        return result





