#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (31.77%)
# Total Accepted:    414K
# Total Submissions: 1.3M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
#
# Example 1:
#
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
#
# Example 2:
#
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
#
#
class Solution:
    # solution 2:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle)-1:
                    return i
        return -1

    '''
    # Solution 1: Your runtime beats 54.39 % of python3 submissions
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle:
            return 0

        if not haystack:
            return -1
        if not needle:
            return 0

        lh, ln = len(haystack), len(needle)
        if lh < ln:
            return -1

        for i in range(lh - ln + 1):
            j = 0
            while j <ln:
                if haystack[i + j] != needle[j]:
                    break
                j +=1

            if j == ln:
                return i
        return -1
    '''

