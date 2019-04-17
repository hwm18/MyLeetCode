#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (35.33%)
# Total Accepted:    329.9K
# Total Submissions: 933.6K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals or len(intervals) <= 1:
            return intervals
        
        intervals = sorted(intervals, key = lambda x: x[0])

        result = []
        for item in intervals:
            if len(result) ==0 or result[-1][1] < item[0]:
               result.append(item)
            else:
                result[-1][1] = max(result[-1][1], item[1])
                
        return result


        

