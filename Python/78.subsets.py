#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (53.01%)
# Likes:    1955
# Dislikes: 50
# Total Accepted:    372.1K
# Total Submissions: 700.4K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
class Solution(object):
    # solution 1: BFS - Your runtime beats 88.99 % of python submissions
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if not nums:
            return ans
        ans.append([])
        for num in nums:
            n = len(ans)
            for i in range(n):
                s = list(ans[i])
                s.append(num)
                ans.append(s)
        return ans
        
    '''
    # DFS recursively 
    def subsets1(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
        
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)
            
    # Bit Manipulation    
    def subsets2(self, nums):
        res = []
        nums.sort()
        for i in xrange(1<<len(nums)):
            tmp = []
            for j in xrange(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res
        
    # Iteratively
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res

    '''
