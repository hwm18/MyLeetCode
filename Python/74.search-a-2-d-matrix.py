#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    '''
    Accepted
    136/136 cases passed (68 ms)
    Your runtime beats 80.52 % of python3 submissions
    Your memory usage beats 27.54 % of python3 submissions (15.9 MB)
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix)==0 or len(matrix[0])==0:
            return False
        
        m,n=len(matrix), len(matrix[0])
        start, end = 0, m*n-1
        while start <= end:  
            mid = start + (end - start) //2

            curr = matrix[mid// n][mid % n]
            if curr == target:
                return True
            
            if curr > target:
                end = mid - 1
            else:
                start = mid + 1

        return False


    '''
    Accepted
    136/136 cases passed (68 ms)
    Your runtime beats 80.52 % of python3 submissions
    Your memory usage beats 18.24 % of python3 submissions (16 MB)
    '''
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix)==0 or len(matrix[0])==0:
            return False
        
        m,n=len(matrix), len(matrix[0])
        start, end = 0, m*n-1
        while start + 1< end:
            mid = start + (end - start) //2

            curr = matrix[mid// n][mid % n]
            if curr == target:
                return True
            
            if curr > target:
                end = mid
            else:
                start = mid 

        if matrix[start//n][start%n] == target:
            return True
        
        if matrix[end//n][end%n] == target:
            return True

        return False
    '''

        
# @lc code=end

