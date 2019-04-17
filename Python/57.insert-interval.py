#
# @lc app=leetcode id=57 lang=python
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (31.02%)
# Total Accepted:    171.4K
# Total Submissions: 552.5K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their
# start times.
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        idx = 0
        while(idx < len(intervals) and intervals[idx][0] < newInterval[0]):
            idx +=1
        
        intervals.insert(idx, newInterval)

        result = []
        for item in intervals:
            if len(result) ==0 or result[-1][1] < item[0]:
               result.append(item)
            else:
                result[-1][1] = max(result[-1][1], item[1])

        return result


        

