#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (44.29%)
# Likes:    5754
# Dislikes: 240
# Total Accepted:    581.7K
# Total Submissions: 1.3M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
# 
# 
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
# 
# 
# Return true if you can finish all courses. Otherwise, return false.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 10^5
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
# 
# 
#

# @lc code=start
class Solution:
    # Solution 1: 拓扑排序 · Topological Sorting
    # 49/49 cases passed (96 ms)
    # Your runtime beats 73.69 % of python3 submissions
    # Your memory usage beats 83.07 % of python3 submissions (15.5 MB)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # build graph
        graph = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses
        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in)
            in_degree[node_in] +=1
        
        #starts = [x for x in graph if in_degree[x]==0]
        queue = collections.deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        count = 0
        while queue:
            node = queue.popleft()
            count +=1
            for next in graph[node]:
                in_degree[next] -= 1
                if in_degree[next]==0:
                    queue.append(next)

        return count == numCourses

        # topoligy sort

        
# @lc code=end

