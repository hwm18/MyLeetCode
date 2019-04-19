#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (51.60%)
# Total Accepted:    323.9K
# Total Submissions: 626.9K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
# 
#
class Solution(object):
    # Your runtime beats 91.54 % of python submissions
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_s = [0] * 256
        len_s, len_t = len(s), len(t)
        if len_s != len_t:
            return False

        for ss in s:
            count_s[ord(ss)] += 1
            
        for tt in t:
            count_s[ord(tt)] -=1
        
        for cs in count_s:
            if cs != 0:
                return False
        
        return True

        

