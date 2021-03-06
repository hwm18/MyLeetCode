#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (55.37%)
# Likes:    2049
# Dislikes: 59
# Total Accepted:    386.4K
# Total Submissions: 696.2K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
from collections import deque
class Solution(object):
    '''
    # soluition 1: BFS - Your runtime beats 95.08 % of python submissions
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if not nums:
            return ans
        q = deque()
        q.append([])
        l = len(nums)
        for idx, num in enumerate(nums):
            n = len(q)
            for _ in range(n):
                old = q.popleft()
                for j in range(len(old)+1):
                    new = list(old)
                    new.insert(j, num)
                    if len(new) == l:
                        ans.append(new)
                    else:
                        q.append(new)
        return ans
  

    # soluition 2: DFS - Your runtime beats 98.82 % of python submissions
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums,[],res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+ [nums[i]], res)
  '''

    # solution 3: DFS
    # 25/25 cases passed (32 ms)
    # Your runtime beats 34.57 % of python submissions
    # Your memory usage beats 15.84 % of python submissions (13.8 MB)
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """        
        if not nums:
            return [[]]
        
        results = []
        self.dfs(nums, set(), [], results)

        return results
    
    def dfs(self, nums, visited, temp, results):
        if len(nums) == len(temp):
            results.append(list(temp))
            return
        
        for i in nums:
            if i in visited:
                continue

            temp.append(i)
            visited.add(i)
            self.dfs(nums, visited, temp, results)
            visited.remove(i)
            temp.pop()

            


