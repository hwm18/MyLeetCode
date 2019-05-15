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

    # solution 2:
    def reverseWords(self, s):
        # strip()去掉s头尾的空格，split()按照空格分割字符串，reversed翻转，''.join按照空格连接字符串
        return " ".join(reversed(s.strip().split()))

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Here sentence is a null-terminated string ending with char '\0'
        if not s or len(s) == 0 or s == "\0":
            return

        s = s.strip()
        # step1: reverse the string
        #  To reverse all words in the string, we will first reverse
        #  the string. Now all the words are in the desired location, but
        #  in reverse order: "Hello World" -> "dlroW olleH".
        self.str_rev(s, 0, len(s) - 2)

        # step2: reverse word by word
        # Now, let's iterate the sentence and reverse each word in place.
        # "dlroW olleH" -> "World Hello"
        start = 0
        end = 0
        while True:
            # find the  start index of a word while skipping spaces.
            while s[start] == " ":
                start += 1

            if s[start] == "\0":
                break

            # find the end index of the word.
            end = start + 1
            while s[end] != "\0" and s[end] != " ":
                end += 1

            # let's reverse the word in-place.
            self.str_rev(s, start, end - 1)
            start = end

    def str_rev(self, str, start, end):
        if str == None or len(str) < 2:
            return

        while start < end:
            temp = str[start]
            # TypeError: 'unicode' object does not support item assignment
            str[start] = str[end]
            str[end] = temp

            start += 1
            end -= 1

