#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (30.70%)
# Total Accepted:    341.2K
# Total Submissions: 1.1M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
#
# Example 1:
#
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
#
# Example 2:
#
#
# Input: "race a car"
# Output: false
#
#
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 0:
            return True

        s = s.strip()
        start, end = 0, len(s)-1
        while start < end:
            while start < end and (not s[start].isalpha() and not s[start].isdigit()):
                start += 1

            while start < end and (not s[end].isalpha() and not s[end].isdigit()):
                end -= 1

            if start >= end:
                return True
            
            if s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False
        
        return True


    '''
    # Your runtime beats 63.47 % of python3 submissions
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 0:
            return True

        s = s.strip()
        n = len(s)
        start, end = 0, n - 1
        while start < end:
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start += 1

            while start < end and not s[end].isalpha() and not s[end].isdigit():
                end -= 1

            if start >= end:
                return True
            if s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False

        return True
    '''

