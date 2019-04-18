#
# @lc app=leetcode id=372 lang=python
#
# [372] Super Pow
#
# https://leetcode.com/problems/super-pow/description/
#
# algorithms
# Medium (35.50%)
# Total Accepted:    26.9K
# Total Submissions: 75.7K
# Testcase Example:  '2\n[3]'
#
# Your task is to calculate a^b mod 1337 where a is a positive integer and b is
# an extremely large positive integer given in the form of an array.
# 
# Example 1:
# 
# 
# 
# Input: a = 2, b = [3]
# Output: 8
# 
# 
# 
# Example 2:
# 
# 
# Input: a = 2, b = [1,0]
# Output: 1024
# 
# 
# 
#
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        num = 0
        for item in b:
            num = num * 10 + item

        b = num
        if b == 0:
            return 1
        if b == 1:
            return a
        result, temp = 1, a
        while(b != 0):
            if (b%2==1):
                result *= temp%1337
            
            temp *= temp%1337
            b /=2
        
        return result%1337
        

