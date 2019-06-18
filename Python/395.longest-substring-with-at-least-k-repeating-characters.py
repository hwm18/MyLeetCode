#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (38.51%)
# Likes:    737
# Dislikes: 68
# Total Accepted:    48.1K
# Total Submissions: 124K
# Testcase Example:  '"aaabb"\n3'
#
#
# Find the length of the longest substring T of a given string (consists of
# lowercase letters only) such that every character in T appears no less than k
# times.
#
#
# Example 1:
#
# Input:
# s = "aaabb", k = 3
#
# Output:
# 3
#
# The longest substring is "aaa", as 'a' is repeated 3 times.
#
#
#
# Example 2:
#
# Input:
# s = "ababbc", k = 2
#
# Output:
# 5
#
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is
# repeated 3 times.
#
#
#
class Solution(object):
    # Solution:  DFS. When all chars in the input string occurs >=k,
    # return the length. But we first need to split the input string by
    # using the characters whose occurrence < k.
    # Your runtime beats 33.03 % of python3 submissions
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        start = 0
        ans = []
        for end in range(len(s)):
            c = s[end]
            count[c] = count.get(c, 0) + 1

        for ss in count:
            if count[ss] < k:
                return max(self.longestSubstring(t, k) for t in s.split(ss))
        return len(s)

