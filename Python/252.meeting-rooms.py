#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#
# https://leetcode.com/problems/meeting-rooms/description/
#
# algorithms
# Easy (53.11%)
# Likes:    436
# Dislikes: 30
# Total Accepted:    108.3K
# Total Submissions: 202.7K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all
# meetings.
#
# Example 1:
#
#
# Input: [[0,30],[5,10],[15,20]]
# Output: false
#
#
# Example 2:
#
#
# Input: [[7,10],[2,4]]
# Output: true
#
#
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
#
#

# @lc code=start
class Solution:
    # Your runtime beats 89.69 % of python3 submissions
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals or len(intervals) == 0:
            return True

        intervals.sort(key=lambda x: x[0])
        """
        pre = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] < pre[1]:
                return False
            pre = curr
        """
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True


# @lc code=end

