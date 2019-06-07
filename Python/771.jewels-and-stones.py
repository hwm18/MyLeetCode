#
# @lc app=leetcode id=771 lang=python
#
# [771] Jewels and Stones
#
# https://leetcode.com/problems/jewels-and-stones/description/
#
# algorithms
# Easy (83.12%)
# Likes:    1436
# Dislikes: 263
# Total Accepted:    257.8K
# Total Submissions: 310.2K
# Testcase Example:  '"aA"\n"aAAbbbb"'
#
# You're given strings J representing the types of stones that are jewels, and
# S representing the stones you have.  Each character in S is a type of stone
# you have.  You want to know how many of the stones you have are also jewels.
# 
# The letters in J are guaranteed distinct, and all characters in J and S are
# letters. Letters are case sensitive, so "a" is considered a different type of
# stone from "A".
# 
# Example 1:
# 
# 
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: J = "z", S = "ZZ"
# Output: 0
# 
# 
# Note:
# 
# 
# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.
# 
# 
#
class Solution(object):
    # Your runtime beats 93.89 % of python submissions
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ans = 0
        for c in S:
            if c in J:
                ans +=1
        return ans
    
    '''
    # solution 1: Your runtime beats 15.6 % of python submissions
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ans = 0
        d = set(a for a in J)
        for a in S:
            if a in d:
                ans +=1
        return ans
    '''
