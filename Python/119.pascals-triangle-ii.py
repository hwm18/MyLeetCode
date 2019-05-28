#
# @lc app=leetcode id=119 lang=python
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (43.52%)
# Likes:    470
# Dislikes: 164
# Total Accepted:    202.9K
# Total Submissions: 466.1K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the k^th index row of the
# Pascal's triangle.
# 
# Note that the row index starts from 0.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 3
# Output: [1,3,3,1]
# 
# 
# Follow up:
# 
# Could you optimize your algorithm to use only O(k) extra space?
# 
#
class Solution(object):
    # our runtime beats 97.07 % of python submissions
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pascal = [1]*(rowIndex + 1)
        for i in range(2, rowIndex +1):
            for j in range(i-1,0,-1):
                pascal[j] += pascal[j-1]
        return pascal

