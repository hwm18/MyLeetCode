#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits/description/
#
# algorithms
# Easy (53.82%)
# Total Accepted:    233.6K
# Total Submissions: 433.8K
# Testcase Example:  '38'
#
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit.
#
# Example:
#
#
# Input: 38
# Output: 2
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
# Since 2 has only one digit, return it.
#
#
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
#
class Solution:
    # Your runtime beats 99.72 % of python3 submissions
    def addDigits(self, num: int) -> int:
        if num >= 0 and num <= 9:
            return num

        while num >= 10:
            sum = 0
            while num > 0:
                sum += num % 10
                num //= 10

            num = sum
        return num

    """
    # Your runtime beats 99.72 % of python3 submissions
    def addDigits(self, num: int) -> int:
        if num >= 0 and num <= 9:
            return num

        result = 0
        while num != 0:
            result = (result * 10 + num % 10) % 9
            num //= 10

        if result == 0:
            result = 9

        return result
    """

