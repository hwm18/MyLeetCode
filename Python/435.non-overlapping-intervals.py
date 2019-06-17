#
# @lc app=leetcode id=435 lang=python
#
# [435] Non-overlapping Intervals
#
# https://leetcode.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (41.59%)
# Likes:    492
# Dislikes: 21
# Total Accepted:    39.5K
# Total Submissions: 95K
# Testcase Example:  '[[1,2]]'
#
# Given a collection of intervals, find the minimum number of intervals you
# need to remove to make the rest of the intervals non-overlapping.
# 
# Note:
# 
# 
# You may assume the interval's end point is always bigger than its start
# point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap
# each other.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [ [1,2], [2,3], [3,4], [1,3] ]
# 
# Output: 1
# 
# Explanation: [1,3] can be removed and the rest of intervals are
# non-overlapping.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [ [1,2], [1,2], [1,2] ]
# 
# Output: 2
# 
# Explanation: You need to remove two [1,2] to make the rest of intervals
# non-overlapping.
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: [ [1,2], [2,3] ]
# 
# Output: 0
# 
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.
# 
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#
class Solution(object):
    # solution 1: your runtime beats 62.92 % of python submissions
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[0])
        res = lo = 0
        for hi in range(1, len(intervals)):
            if intervals[lo][1] > intervals[hi][0]: #overlap
                res += 1
            if not intervals[hi][0] < intervals[lo][1] < intervals[hi][1]:
                lo = hi
        return res
        

