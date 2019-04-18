#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (42.73%)
# Total Accepted:    553.2K
# Total Submissions: 1.3M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
#
# Example 1:
#
#
# Input: 121
# Output: true
#
#
# Example 2:
#
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
#
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
# Follow up:
#
# Coud you solve it without converting the integer to a string?
#
#
class Solution:
    # Your runtime beats 89.86 % of python3 submissions
    # 翻转整数，判断是否相等
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x >= 0 and x <= 9:
            return True

        new_x = 0
        temp_x = x
        while temp_x != 0:
            new_x = new_x * 10 + temp_x % 10
            temp_x //= 10

        return new_x == x

    """
    # Your runtime beats 79.56 % of python3 submissions
    def isPalindrome(self, x: int) -> bool:
        if not x or len(str(x)) == 1:
            return True

        # convert to string and use two points
        new_str = str(x)
        if new_str[0] == "-":
            return False
        if new_str[0] == "+":
            new_str = new_str[1:]
        n = len(new_str)
        start, end = 0, n - 1
        while start < end:
            if new_str[start] == new_str[end]:
                start += 1
                end -= 1
            else:
                return False

        return start >= end
    """

    """
    # Your runtime beats 82.65 % of python3 submissions
    # reverse string and compare the integer
    def isPalindrome(self, x: int) -> bool:
        if not x or len(str(x)) == 1:
            return True
        new_str = str(x)
        if new_str[0] == "-":
            return False
        if new_str[0] == "+":
            new_str = new_str[1:]

        new_str = new_str[::-1]

        return int(new_str) == x
    """

