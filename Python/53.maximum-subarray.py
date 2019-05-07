#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
class Solution:
    # method 2: Your runtime beats 93.05 % of python3 submissions
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums and len(nums)==0:
            return 0
        
        n = len(nums)
        dp = [0] * n
        dp[0],result = nums[0],nums[0]
        for i in range(1,n):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            result = max(result, dp[i])
        return result

    '''
    # Method 1: Your runtime beats 64.36 % of python3 submissions
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums and len(nums)==0:
            return 0
        
        currMax, result = nums[0],nums[0]
        for num in nums[1:]:
            currMax = max(currMax+num, num)
            result = max(result, currMax)
        return result
    '''
        

