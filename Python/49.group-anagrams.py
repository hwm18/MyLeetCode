#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (46.70%)
# Likes:    1628
# Dislikes: 108
# Total Accepted:    337K
# Total Submissions: 720.5K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#
class Solution(object):
    # Your runtime beats 95.77 % of python submissions
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return [[]]
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            #d[key] = d.get(key, []) + [w]
            if key not in d:
                d[key] = []
            d[key].append(w)
        return d.values()

        

