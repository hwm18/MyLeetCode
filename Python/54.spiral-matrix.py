#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (30.41%)
# Likes:    1064
# Dislikes: 405
# Total Accepted:    233K
# Total Submissions: 766.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#
class Solution(object):
    # solution 2: Your runtime beats 98.87 % of python submissions
    # 22/22 cases passed (16 ms)
    # Your runtime beats 72.82 % of python submissions
    # Your memory usage beats 40.26 % of python submissions (13.5 MB)
    def spiralOrder(self, matrix):
        # return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])
        result = []
        if not matrix or len(matrix[0])==0:
            return result        
        
        m,n=len(matrix), len(matrix[0])
        row, col = 0,-1

        while True:
            # go right
            for i in range(n):
                col +=1
                result.append(matrix[row][col])
                            
            m = m -1
            if m == 0:
                break
            # go down
            for i in range(m):
                row += 1
                result.append(matrix[row][col])
                
            n = n -1
            if n==0:
                break

            # go left
            for i in range(n):
                col -= 1
                result.append(matrix[row][col])
                
            m -= 1
            if m ==0:
                break

            # go up
            for i in range(m):
                row -= 1
                result.append(matrix[row][col])
                
            n -= 1
            if n==0:
                break
        
        return result





    '''
    # solution 1: Your runtime beats 68.81 % of python submissions
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix)==0 or len(matrix[0])==0:
            return []
        up, left = 0,0
        down = len(matrix)-1
        right = len(matrix[0])-1
        direct = 0  # 0: go right   1: go down  2: go left  3: go up
        res = []
        while True:
            if direct == 0:
                for i in range(left, right+1):
                    res.append(matrix[up][i])
                up += 1
            if direct == 1:
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1
            if direct == 2:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if direct == 3:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1
            if up > down or left > right: 
                return res
            direct = (direct+1) % 4
    '''
            
            


