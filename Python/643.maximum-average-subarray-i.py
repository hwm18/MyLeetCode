#
# @lc app=leetcode id=643 lang=python
#
# [643] Maximum Average Subarray I
#
# https://leetcode.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (39.57%)
# Likes:    460
# Dislikes: 84
# Total Accepted:    52.2K
# Total Submissions: 131.8K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# Given an array consisting of n integers, find the contiguous subarray of
# given length k that has the maximum average value. And you need to output the
# maximum average value.
# 
# Example 1:
# 
# 
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].
# 
# 
# 
# 
#
class Solution(object):
    # slide window:  Your runtime beats 30.03 % of python submissions
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if not nums or k<1:
            return 0
        ans = -(1<<32)
        windowSum,windowStart =0.0,0
        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            if windowEnd >= k-1:
                ans = max(ans, windowSum/k)
                windowSum -= nums[windowStart]
                windowStart +=1
        return ans



