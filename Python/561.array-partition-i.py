#
# @lc app=leetcode id=561 lang=python
#
# [561] Array Partition I
#
# https://leetcode.com/problems/array-partition-i/description/
#
# algorithms
# Easy (68.99%)
# Likes:    562
# Dislikes: 1693
# Total Accepted:    143.7K
# Total Submissions: 208.3K
# Testcase Example:  '[1,4,3,2]'
#
# 
# Given an array of 2n integers, your task is to group these integers into n
# pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of
# min(ai, bi) for all i from 1 to n as large as possible.
# 
# 
# Example 1:
# 
# Input: [1,4,3,2]
# 
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3,
# 4).
# 
# 
# 
# Note:
# 
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].
# 
# 
#
class Solution(object):
    # solution 2: Your runtime beats 40.86 % of python submissions
    def arrayPairSum(self, nums):
		nums = sorted(nums)     # to make it as big as possible, array should be sorted
		result = 0      # sum will be stored here
		for i in range(0, len(nums) - 1, 2):        # iterate from first to second last counting every second element
			result += min(nums[i], nums[i+1])       # get min and add to the result

		return result

    '''
    # solution 1:  Your runtime beats 65.31 % of python submissions
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==0:
            return 0
        nums = sorted(nums)
        ans = 0
        i = 0
        # [1,2,3,2]
        while i < len(nums)-1:
            ans += nums[i]
            i += 2
        return ans
    '''

        

