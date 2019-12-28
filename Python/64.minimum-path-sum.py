#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    # solution 1: DP: dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
    # Your runtime beats 94.7 % of python3 submissions
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or len(grid)==0 or len(grid[0])==0:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0]=grid[0][0]

        for j in range(1,n):
            dp[0][j] = dp[0][j-1]+grid[0][j]
        
        for i in range(1,m):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]= min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        
        return dp[m-1][n-1]
    
    '''
    # DP: Your runtime beats 98.34 % of python3 submissions
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]

        for i in range(1, m):
            grid[i][0] += grid[i-1][0]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
    '''
        
# @lc code=end

