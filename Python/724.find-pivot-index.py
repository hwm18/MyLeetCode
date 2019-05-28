#
# @lc app=leetcode id=724 lang=python
#
# [724] Find Pivot Index
#
# https://leetcode.com/problems/find-pivot-index/description/
#
# algorithms
# Easy (41.06%)
# Likes:    593
# Dislikes: 149
# Total Accepted:    68.5K
# Total Submissions: 166.7K
# Testcase Example:  '[1,7,3,6,5,6]'
#
# Given an array of integers nums, write a method that returns the "pivot"
# index of this array.
# 
# We define the pivot index as the index where the sum of the numbers to the
# left of the index is equal to the sum of the numbers to the right of the
# index.
# 
# If no such index exists, we should return -1. If there are multiple pivot
# indexes, you should return the left-most pivot index.
# 
# Example 1:
# 
# 
# Input: 
# nums = [1, 7, 3, 6, 5, 6]
# Output: 3
# Explanation: 
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the
# sum of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# nums = [1, 2, 3]
# Output: -1
# Explanation: 
# There is no index that satisfies the conditions in the problem
# statement.
# 
# 
# 
# 
# Note:
# 
# 
# The length of nums will be in the range [0, 10000].
# Each element nums[i] will be an integer in the range [-1000, 1000].
# 
# 
# 
# 
#
class Solution(object):
    # soluiton 2: Your runtime beats 63.41 % of python submissions
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, sum(nums)
        for i, num in  enumerate(nums):
            right -= num
            if left == right:
                return i
            left += num
        return -1

    '''
    # soluiton 1: 从左向右枚举中心索引
    # Your runtime beats 63.41 % of python submissions
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # total: 28
        # idx: 0-> (28-1)/2= 13.5  1-> (28-7)/2=10.5, 2-> 12.5, 3->11
        # subSum: 0                 1                  8      11
        if not nums or len(nums)==0:
            return -1
        
        total = sum(nums)        
        leftSum = 0
        for i in range(len(nums)):
            if i != 0:
                leftSum += nums[i-1]
            if leftSum == total -leftSum - nums[i]:
                return i
        
        return -1
    '''


