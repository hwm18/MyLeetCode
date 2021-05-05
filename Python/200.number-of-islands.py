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
    # Solution 2: BFS
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]

        n, m = len(grid), len(grid[0])
        num = 0
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and (i,j) not in visited:
                    self.bfs(grid,i,j, visited)
                    num+=1
        
        return num
    
    def bfs(self, grid, row, col, visited):
        queue = collections.deque([(row, col)])
        visited.add((row, col))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                newXX = x + self.dx[i]
                newYY = y + self.dy[i]
                if not self.isValid(grid,newXX,newYY, visited):
                    continue

                queue.append((newXX,newYY))
                visited.add((newXX,newYY))
        
    
    def isValid(self, grid, x, y, visited):
        n,m=len(grid), len(grid[0])
        if not ( 0<= x <n and 0<=y<m):
            return False
        
        if (x,y) in visited:
            return False
        
        return grid[x][y] =='1'           
             


    '''
    # solution 1:  DFS. Iterate through each of the cell and if it is an island, 
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
    '''


# @lc code=end

