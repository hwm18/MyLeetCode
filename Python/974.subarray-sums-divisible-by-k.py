#
# @lc app=leetcode id=974 lang=python
#
# [974] Subarray Sums Divisible by K
#
# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (44.77%)
# Likes:    274
# Dislikes: 25
# Total Accepted:    11.6K
# Total Submissions: 25.9K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# Given an array A of integers, return the number of (contiguous, non-empty)
# subarrays that have a sum divisible by K.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000
# 
# 
#
class Solution(object):
    # Your runtime beats 62.6 % of python submissions
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        ans = 0
        sum = 0
        d = {0:1}
        for end, num in enumerate(A):
            sum +=num
            key = sum %K
            
            if key in d:
                ans += d[key]
                d[key] += 1
            else:
                d[key] = 1
                
        return ans
            
            
        

