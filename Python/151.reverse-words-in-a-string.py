#
# @lc app=leetcode id=151 lang=python
#
# [151] Reverse Words in a String
#
# https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (16.61%)
# Likes:    541
# Dislikes: 2240
# Total Accepted:    277.3K
# Total Submissions: 1.7M
# Testcase Example:  '"the sky is blue"'
#
# Given an input string, reverse the string word by word.
#
#
#
# Example 1:
#
#
# Input: "the sky is blue"
# Output: "blue is sky the"
#
#
# Example 2:
#
#
# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing
# spaces.
#
#
# Example 3:
#
#
# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single
# space in the reversed string.
#
#
#
#
# Note:
#
#
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed
# string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the
# reversed string.
#
#
#
#
# Follow up:
#
# For C programmers, try to solve it in-place in O(1) extra space.
#
class Solution(object):
    """
    # solution 1:
    def reverseWords(self, s):
        return " ".join(s.strip().split()[::-1])
    """
    
    '''
    # solution 2: Your runtime beats 64.71 % of python submissions
    def reverseWords(self, s):
        # strip()去掉s头尾的空格，split()按照空格分割字符串，reversed翻转，''.join按照空格连接字符串
        return " ".join(reversed(s.strip().split()))

    '''

    # Solution 1: Your runtime beats 64.71 % of python submissions
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Here sentence is a null-terminated string ending with char '\0'
        if not s or len(s) == 0: #or s == "\0":
            return s

        s = s.strip()
        if s == "":
            return s

        # keep only one space for words
        arr = s.split()
        results = []
        for i in range(len(arr)-1,-1,-1):
            if arr[i] !="":
                results.append(arr[i])
        
        return " ".join(results)

    def str_rev(self, str, start, end):
        if str == None or len(str) < 2:
            return
        
        l =list(str)
        while start < end:
            l[start], l[end] = l[end], l[start]  # swap the start and end

            start += 1
            end -= 1
        return ''.join(l)

