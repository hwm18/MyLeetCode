#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (22.12%)
# Total Accepted:    250.5K
# Total Submissions: 1.1M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
# 
# Example 1:
# 
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
# 
#
# Your runtime beats 88.11 % of python submissions
class Solution(object):
    '''
    "226" -> f[n] = f[n-1] (s[n]!=0) + f[n-2] (s[n] * 10+s[n-1] in [10,26])
    '''
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0

        if(len(s) ==1):
            return 1

        result = [1,1]
        for i in range(2, len(s)+1):            
            first = result[-1]
            second = result[-2]
            two = int(s[i-2:i])
            if( 10<=two <=26 and s[i-1] !='0'):            
                result.append(first + second)
            elif(two ==10 or two ==20):
                result.append(second)
            elif(s[i-1] !='0'):
                result.append(first)
            else:
                return 0
            
        return result[-1]
        

