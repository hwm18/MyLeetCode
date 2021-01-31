#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (29.54%)
# Likes:    8157
# Dislikes: 579
# Total Accepted:    1.1M
# Total Submissions: 3.5M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# Example 3:
# 
# 
# Input: s = "a"
# Output: "a"
# 
# 
# Example 4:
# 
# 
# Input: s = "ac"
# Output: "a"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),
# 
# 
#

# @lc code=start
class Solution:
    '''
    176/176 cases passed (956 ms)
    Your runtime beats 77.07 % of python3 submissions
    Your memory usage beats 31.54 % of python3 submissions (14.2 MB)
    '''
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s)==0:
            return s
        
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s,i,i)
            if len(tmp) > len(res):
                res = tmp
            
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        
        return res
    
    def helper(self, s, l, r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        
        return s[l+1: r]
    

        
# @lc code=end

