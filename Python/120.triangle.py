#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (45.59%)
# Likes:    3093
# Dislikes: 319
# Total Accepted:    312.8K
# Total Submissions: 666.2K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle array, return the minimum path sum from top to bottom.
# 
# For each step, you may move to an adjacent number of the row below. More
# formally, if you are on index i on the current row, you may move to either
# index i or index i + 1 on the next row.
# 
# 
# Example 1:
# 
# 
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
# ⁠  2
# ⁠ 3 4
# ⁠6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined
# above).
# 
# 
# Example 2:
# 
# 
# Input: triangle = [[-10]]
# Output: -10
# 
# 
# 
# Constraints:
# 
# 
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -10^4 <= triangle[i][j] <= 10^4
# 
# 
# 
# Follow up: Could you do this using only O(n) extra space, where n is the
# total number of rows in the triangle?
#

# @lc code=start
class Solution:
    # solution 1: 使用记忆化搜索的版本 时间复杂度 O(n2) 空间复杂度 O(n2)（额外耗费的空间）
    # 43/43 cases passed (68 ms)
    # Your runtime beats 23.85 % of python3 submissions
    # Your memory usage beats 12.17 % of python3 submissions (17.2 MB)
    '''
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.devide_conquer(triangle, 0,0,{})
    
    # 函数返回从 x, y 出发，走到最底层的最短路径值
    # memo 中 key 为二元组 (x, y)
    # memo 中 value 为从 x, y 走到最底层的最短路径值
    def devide_conquer(self, triangel, x, y, memo):
        if x == len(triangel):
            return 0
        
        # 如果找过了，就不要再找了，直接把之前找到的值返回
        if (x, y) in memo:
            return memo[(x,y)]
        
        left = self.devide_conquer(triangel, x+1, y, memo)
        right = self.devide_conquer(triangel, x+1, y+1, memo)

        # 在 return 之前先把这次找到的最短路径值记录下来
        # 避免之后重复搜索
        memo[(x,y)]= min(left, right) + triangel[x][y]

        return memo[(x,y)]
    '''

    # solution 2: 自顶向下的方式的多重循环动态规划 使用了滚动数组优化空间 时间复杂度 O(n2) 空间复杂度 O(n) （额外空间）
    def minimumTotal(self, triangle):
        n = len(triangle)
        
        # state: dp[i][j] 代表从 0, 0 走到 i, j 的最短路径值
        dp = [[0] * n, [0] * n]
        
        # initialize: 初始化起点
        dp[0][0] = triangle[0][0]
        
        # function: dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        # i, j 这个位置是从位置 i - 1, j 或者 i - 1, j - 1 走过来的
        for i in range(1, n):
            dp[i % 2][0] = dp[(i - 1) % 2][0] + triangle[i][0]
            dp[i % 2][i] = dp[(i - 1) % 2][i - 1] + triangle[i][i]
            for j in range(1, i):
                dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[(i - 1) % 2][j - 1]) + triangle[i][j]
               
        # answer: 最后一层的任意位置都可以是路径的终点
        return min(dp[(n - 1) % 2])
        
# @lc code=end

