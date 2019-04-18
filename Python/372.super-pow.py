#
# @lc app=leetcode id=372 lang=python
#
# [372] Super Pow
#
# https://leetcode.com/problems/super-pow/description/
#
# algorithms
# Medium (35.50%)
# Total Accepted:    26.9K
# Total Submissions: 75.7K
# Testcase Example:  '2\n[3]'
#
# Your task is to calculate a^b mod 1337 where a is a positive integer and b is
# an extremely large positive integer given in the form of an array.
#
# Example 1:
#
#
#
# Input: a = 2, b = [3]
# Output: 8
#
#
#
# Example 2:
#
#
# Input: a = 2, b = [1,0]
# Output: 1024
#
#
#
#
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        mod = 1337
        a %= mod
        result = 1
        for item in reversed(b):
            result = result * self.powerHelper(a, item, mod) % mod
            a = self.powerHelper(a, 10, mod) % mod
        return result

    def powerHelper(self, a, b, mod):
        a %= mod
        result = 1
        while b != 0:
            if (b & 1) != 0:
                result = result * a % mod

            a = a * a % mod
            b >>= 1

        return result

