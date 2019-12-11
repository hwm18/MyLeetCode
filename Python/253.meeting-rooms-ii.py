#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (43.85%)
# Likes:    1934
# Dislikes: 32
# Total Accepted:    215.4K
# Total Submissions: 487.2K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
# required.
#
# Example 1:
#
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
#
# Example 2:
#
#
# Input: [[7,10],[2,4]]
# Output: 1
#
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
#
#

# @lc code=start
class Solution:
    # solution 1: use min heap
    # Your runtime beats 97.88 % of python3 submissions
    import heapq

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 0:
            return 0

        max_room = 0
        rooms = []
        intervals.sort(key=lambda x: x[0])  # sort by start time
        for item in intervals:
            heapq.heappush(rooms, item[1])
            while rooms[0] <= item[0]:
                heapq.heappop(rooms)
            max_room = max(max_room, len(rooms))
        return max_room

    """
    # Solution2: Your runtime beats 99.49 % of python3 submissions
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 0:
            return 0

        starts, ends = [], []
        for item in intervals:
            starts.append(item[0])
            ends.append(item[1])

        # sort
        starts.sort()
        ends.sort()

        numRooms, available = 0, 0
        s, e = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                if available == 0:
                    numRooms += 1
                else:
                    available -= 1
                s += 1
            else:
                available += 1
                e += 1
        return numRooms
    """


# @lc code=end

