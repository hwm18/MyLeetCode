#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (42.37%)
# Likes:    3688
# Dislikes: 167
# Total Accepted:    394.9K
# Total Submissions: 914.6K
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
# Return the ordering of courses you should take to finish all courses. If
# there are many valid answers, return any of them. If it is impossible to
# finish all courses, return an empty array.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished course 0. So the correct course order is [0,1].
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both courses 1 and 2. Both courses 1 and 2 should be
# taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3].
# 
# 
# Example 3:
# 
# 
# Input: numCourses = 1, prerequisites = []
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.
# 
# 
#

# @lc code=start
class Solution:
    # Solution 1: 拓扑排序 · Topological Sorting
    # 44/44 cases passed (92 ms)
    # Your runtime beats 93.63 % of python3 submissions
    # Your memory usage beats 99.03 % of python3 submissions (15.3 MB)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # build graph
        graph = [[] for i in range(numCourses)]
        indegrees = [0] * numCourses

        for curr, pre in prerequisites:
            graph[pre].append(curr)
            indegrees[curr] += 1
            
        # topological sorting        
        topsort = []
        # queue = collections.deque()
        # for i in range(numCourses):
        #     if indegrees[i]==0:
        #         queue.append(i)
        starts = [i for i in range(numCourses) if indegrees[i]==0]
        queue = collections.deque(starts)

            
        while queue:
            node = queue.popleft()
            topsort.append(node)
            for next in graph[node]:
                indegrees[next] -= 1
                if indegrees[next]==0:
                    queue.append(next)
        
        if len(topsort)==numCourses:
            return topsort
        
        return []
        
# @lc code=end

