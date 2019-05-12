#
# @lc app=leetcode id=154 lang=python
#
# [154] Find Minimum in Rotated Sorted Array II
#
class Solution(object):
    # Your runtime beats 47.11 % of python submissions
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==0:
            return  -1
        n = len(nums)
        ans = 1<<31
        for i in nums:
            if i < ans:
                ans = i
        return ans

