#
# @lc app=lintcode id=180 lang=python
#
# [180] binary representation
#
# https://www.lintcode.com/problem/binary-representation/description
#
# Given a(decimal - e.g. 3.72) number that is passed in as a string, return the binary representation that is passed in as a string.
# If the fractional part of the number can not be represented accurately in binary with at most 32 characters, return ERROR.
#
# Example 1
# Input: "3.72"
# Output: "ERROR"
# Explanation: (3.72)​10​​ =(11.10111000010100011111⋯)​2​​  We can't represent it in 32 characters.

# Example 2
# Input: "3.5"
# OUtput: "11.1"
# Explanation: (3.5)​10​​ =(11.1)​2
#
#
from decimal import *


class Solution(object):
    """
    @param n: Given a decimal number that is passed in as a string
    @return: A string
    """

    # Your submission beats 96.23% Submissions!
    def binaryRepresentation(self, n):
        if n == "0" or n == "1":
            return n

        (a, b) = n, "0"
        if "." in n:
            (a, b) = n.split(".")

        a = "{:b}".format(int(a))
        b = self.frac_to_binary(b)

        if b is None:
            return "ERROR"
        if b == "":
            return a
        return a + "." + b

    def frac_to_binary(self, num):
        if int(num) == 0:
            return ""
        if int(num) % 10 != 5:
            return None

        res = ""
        num = Decimal("0." + str(num))
        while num:
            num *= 2
            if num >= 1:
                res += "1"
                num -= 1
            else:
                res += "0"
            num = num.normalize()
            if num and str(num)[-1] != "5":
                return None
        return res

