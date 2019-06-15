#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (42.51%)
# Likes:    885
# Dislikes: 50
# Total Accepted:    205.5K
# Total Submissions: 482.7K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
# 
#
class Solution(object):
    #Soluiton 2: BFS - Your runtime beats 89.86 % of python submissions
    # if S[i] is same to S[i - 1], then it needn’t to be added to all of the subset, 
    # just add it to the last l subsets which are created by adding S[i - 1]
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        list.sort(nums)
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res

    '''
    # Soluiton 1: BFS - Your runtime beats 96.96 % of python submissions
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        if not nums:
            return subsets
        
        # sort the numbers to handle duplicates
        list.sort(nums)
        
        subsets.append([])
        startIndex, endIndex = 0, 0
        for idx, num in enumerate(nums):
            startIndex = 0
            # if current and the previous elements are same, create new subsets only from the subsets
            # added in the previous step
            if idx > 0 and nums[idx] == nums[idx - 1]:
                startIndex = endIndex + 1
            endIndex = len(subsets) - 1
            for j in range(startIndex, endIndex+1):
                # create a new subset from the existing subset and add the current element to it
                set = list(subsets[j])
                set.append(num)
                subsets.append(set)
        return subsets
    '''

