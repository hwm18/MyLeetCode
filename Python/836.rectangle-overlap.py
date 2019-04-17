#
# @lc app=leetcode id=836 lang=python
#
# [836] Rectangle Overlap
#
# https://leetcode.com/problems/rectangle-overlap/description/
#
# algorithms
# Easy (46.14%)
# Total Accepted:    22.1K
# Total Submissions: 47.8K
# Testcase Example:  '[0,0,2,2]\n[1,1,3,3]'
#
# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the
# coordinates of its bottom-left corner, and (x2, y2) are the coordinates of
# its top-right corner.
# 
# Two rectangles overlap if the area of their intersection is positive.  To be
# clear, two rectangles that only touch at the corner or edges do not overlap.
# 
# Given two (axis-aligned) rectangles, return whether they overlap.
# 
# Example 1:
# 
# 
# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false
# 
# 
# Notes:
# 
# 
# Both rectangles rec1 and rec2 are lists of 4 integers.
# All coordinates in rectangles will be between -10^9 and 10^9.
# 
# 
# Your runtime beats 76.61 % of python submissions
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if not rec1 or not rec2:
            return False

        # [x1, y1, x2, y2]
        x1_rec1, y1_rec1, x2_rec1, y2_rec1 = rec1[0], rec1[1], rec1[2], rec1[3]
        x1_rec2, y1_rec2, x2_rec2, y2_rec2 = rec2[0], rec2[1], rec2[2], rec2[3]
        # left and right
        if x2_rec1 <= x1_rec2 or x1_rec1 >= x2_rec2:
            return False

        # up and down
        if y1_rec1 >= y2_rec2 or y2_rec1 <= y1_rec2:
            return False

        return True
        

