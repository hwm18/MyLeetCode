#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.24%)
# Total Accepted:    657.1K
# Total Submissions: 2.6M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#
class Solution(object):
    '''
    1032/1032 cases passed (32 ms)
    Your runtime beats 9.44 % of python submissions
    Your memory usage beats 40.77 % of python submissions (13.4 MB)
    '''
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x or len(str(x)) <= 1:
            return x

        neg = 1
        if x < 0:
            neg, x = -1, -x
        
        result = 0
        while(x != 0):
            result = result * 10 + x % 10
            x //= 10

        result *= neg
        if (abs(result)>(1<<31)):
            return 0

        return result
    


