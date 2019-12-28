#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
# Tags:   algorithms   amazon   facebook   google   microsoft   zenefits   depth-first-search   breadth-first-search   union-find

# Langs:  c   cpp   csharp   golang   java   javascript   kotlin   php   python   python3   ruby   rust   scala   swift

# * algorithms
# * Medium (43.26%)
# * Likes:    3633
# * Dislikes: 133
# * Total Accepted:    491.7K
# * Total Submissions: 1.1M
# * Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'

# <p>Given a 2d grid map of <code>&#39;1&#39;</code>s (land) and <code>&#39;0&#39;</code>s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.</p>

# <p><b>Example 1:</b></p>

# <pre>
# <strong>Input:</strong>
# 11110
# 11010
# 11000
# 00000

# <strong>Output:</strong>&nbsp;1
# </pre>
#
#

# @lc code=start
class Solution:
    # solution: Iterate through each of the cell and if it is an island, 
    # do dfs to mark all adjacent islands, then increase the counter by 1.
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0

        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]

        n, m = len(grid), len(grid[0])
        num = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    num += 1

        return num

    def dfs(self, grid, row, col):
        if (
            row >= len(grid)
            or row < 0
            or col >= len(grid[0])
            or col < 0
            or grid[row][col] != "1"
        ):
            return

        grid[row][col] = "0" # or '#' - update the element value

        # Your runtime beats 42.71 % of python3 submissions
        # for i in range(4):
        #     newRow = row + self.dx[i]
        #     newCol = col + self.dy[i]
        #     if (
        #         newRow < len(grid)
        #         and newRow >= 0
        #         and newCol < len(grid[0])
        #         and newCol >= 0
        #         and grid[newRow][newCol] == "1"
        #     ):
        #         self.dfs(grid, newRow, newCol)

        # Your runtime beats 93.81 % of python3 submissions
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)


# @lc code=end

