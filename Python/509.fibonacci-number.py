#
# @lc app=leetcode id=509 lang=python
#
# [509] Fibonacci Number
#
# https://leetcode.com/problems/fibonacci-number/description/
#
# algorithms
# Easy (66.73%)
# Likes:    157
# Dislikes: 135
# Total Accepted:    50.1K
# Total Submissions: 75.1K
# Testcase Example:  '2'
#
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
# Fibonacci sequence, such that each number is the sum of the two preceding
# ones, starting from 0 and 1. That is,
#
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
#
#
# Given N, calculate F(N).
#
#
#
# Example 1:
#
#
# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
#
#
# Example 2:
#
#
# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
#
#
# Example 3:
#
#
# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
#
#
#
#
# Note:
#
# 0 ≤ N ≤ 30.
#
#
class Solution(object):
    # soluiton 2: dynamic program
    # Your runtime beats 99.25 % of python submissions
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 2:
            return N

        # f[n] = f[n-1] +f[n-2]
        # n1 is f[n-1] and n2 is f[n-2]
        n1, n2, ans = 1, 0, 0
        for _ in range(2, N + 1):
            ans = n1 + n2
            n2 = n1
            n1 = ans
        return ans

    '''
    # solution 1: recursion -Your runtime beats 24.5 % of python submissions
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 2:
            return N
        return self.fib(N - 1) + self.fib(N - 2)
    '''

