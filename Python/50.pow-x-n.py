#
# @lc app=leetcode id=50 lang=python
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (27.78%)
# Total Accepted:    307.7K
# Total Submissions: 1.1M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (x^n).
# 
# Example 1:
# 
# 
# Input: 2.00000, 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: 2.10000, 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# Note:
# 
# 
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
# 
# 
# 
class Solution(object):
    '''
    # Your runtime beats 96.63 % of python submissions
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        
        half = self.myPow(x, n/2)

        result = half * half
        if(n%2 ==1):
            result *= x 
        
        return result
    '''

    # Your runtime beats 76.1 % of python submissions
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -n
            x = 1/x

        result = 1
        while n:
            if n & 1:
                result *= x

            x *= x
            n >>= 1
        
        return result

    '''
    # Your runtime beats 43.99 % of python submissions
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        
        if n<0:
            return 1/self.myPow(x,-n)
        
        if n%2:
            return x * self.myPow(x, n-1)
        
        return self.myPow(x * x, n//2)
    '''


           

