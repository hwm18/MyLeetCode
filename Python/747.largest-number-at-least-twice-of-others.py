#
# @lc app=leetcode id=747 lang=python
#
# [747] Largest Number At Least Twice of Others
#
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
#
# algorithms
# Easy (40.50%)
# Likes:    197
# Dislikes: 403
# Total Accepted:    50.2K
# Total Submissions: 124K
# Testcase Example:  '[0,0,0,1]'
#
# In a given integer array nums, there is always exactly one largest element.
# 
# Find whether the largest element in the array is at least twice as much as
# every other number in the array.
# 
# If it is, return the index of the largest element, otherwise return -1.
# 
# Example 1:
# 
# 
# Input: nums = [3, 6, 1, 0]
# Output: 1
# Explanation: 6 is the largest integer, and for every other number in the
# array x,
# 6 is more than twice as big as x.  The index of value 6 is 1, so we return
# 1.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1, 2, 3, 4]
# Output: -1
# Explanation: 4 isn't at least as big as twice the value of 3, so we return
# -1.
# 
# 
# 
# 
# Note:
# 
# 
# nums will have a length in the range [1, 50].
# Every nums[i] will be an integer in the range [0, 99].
# 
# 
# 
# 
#
class Solution(object):
    # Your runtime beats 63.62 % of python submissions
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==0:
            return -1
        ans,ansValue,second = -1, -(1<<31),0
        for i, num in enumerate(nums):
            if num>=ansValue:
                second = ansValue
                ansValue = num
                ans = i
            # [0,0,3,2]
            elif num >= second:
                second = num
        if ansValue >= second * 2:
            return ans
        return -1
