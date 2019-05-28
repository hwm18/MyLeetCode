#
# @lc app=leetcode id=209 lang=python
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (34.84%)
# Likes:    1088
# Dislikes: 66
# Total Accepted:    176.5K
# Total Submissions: 506.6K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# Example: 
# 
# 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
# 
#
class Solution(object):
    # solution 1: two points - Your runtime beats 60.53 % of python submissions
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==0:
            return 0
        
        ans, n = (1<<31),len(nums)
        slow,fast =0,0
        currSum =0
        while currSum < s:
            currSum += nums[fast]
            fast +=1

            while currSum >=s:
                if fast - slow < ans:
                    ans = fast - slow 
                currSum -= nums[slow]
                slow +=1
            if fast == n:
                break
        if ans > n:
            return 0
        return ans



        

