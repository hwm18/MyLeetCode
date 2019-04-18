#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (44.75%)
# Total Accepted:    224.3K
# Total Submissions: 500.9K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
#
# Example:
#
#
# Input: 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
# Your runtime beats 77.64 % of python3 submissions
class Solution:
    # 看看变化的过程中，是否出现重复，若出现，则代表不是快乐数
    def isHappy(self, n: int) -> bool:
        d = {}
        while True:
            d[n] = 1
            n = sum([int(x) * int(x) for x in list(str(n))])
            if n == 1 or n in d:
                break

        return n == 1

