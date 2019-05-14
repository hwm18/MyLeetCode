#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
class Solution:
    # Your runtime beats 88.34 % of python3 submissions
    def isPerfectSquare(self, num: int) -> bool:
        if not num or num < 0:
            return False

        if num in (0, 1):
            return True

        start, end = 2, num
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid == num / mid:
                return True

            if mid > num / mid:
                end = mid
            else:
                start = mid

        if start == num / start:
            return True
        if end == num / end:
            return True
        return False

