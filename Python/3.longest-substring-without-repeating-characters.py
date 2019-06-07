#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (28.41%)
# Likes:    5595
# Dislikes: 313
# Total Accepted:    941.9K
# Total Submissions: 3.3M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#
class Solution(object):
    # solution 2: Your runtime beats 98.97 % of python submissions
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        start = ans = 0
        usedChar = {}
        for i,c in enumerate(s):
            if c in usedChar and start <=usedChar[c]:
                start = usedChar[c] + 1
            else:
                ans = max(ans, i - start + 1)
            usedChar[c] = i

        return ans

    '''
    # solution 1: Your runtime beats 8 % of python submissions
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        ans = 0
        
        #i,j=0,0
        for i in range(len(s)):
            d = set(s[i])
            j = i+1
            while j<len(s) and s[j] not in d:
                d.add(s[j])
                j +=1
            ans = max(ans, len(d))
        return ans
    '''
            
            
                
        

