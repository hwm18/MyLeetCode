#
# @lc app=leetcode id=485 lang=python
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (55.04%)
# Likes:    361
# Dislikes: 307
# Total Accepted:    136.8K
# Total Submissions: 248.5K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# Given a binary array, find the maximum number of consecutive 1s in this
# array.
# 
# Example 1:
# 
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s.
# ⁠   The maximum number of consecutive 1s is 3.
# 
# 
# 
# Note:
# 
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# 
# 
#
class Solution(object):
    # solution 2:  Your runtime beats 47.82 % of python submissions
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts=[]
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count=count+1
            else:
                counts.append(count)
                count=0
        counts.append(count)
        return max(counts)

    '''
    # solution 1: Your runtime beats 18.79 % of python submissions
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==0:
            return 0
        
        # [1,1,0,1,1,1]
        ans,cnt,right=0,0,0
        while right < len(nums):
            if nums[right]==0:
                ans = max(ans, cnt)
                cnt = 0
            else:
                cnt+=1
        
            right +=1
        ans = max(ans, cnt)

        return  ans
    '''



