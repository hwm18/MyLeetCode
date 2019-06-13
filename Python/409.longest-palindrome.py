#
# @lc app=leetcode id=409 lang=python
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (48.07%)
# Likes:    524
# Dislikes: 56
# Total Accepted:    97.7K
# Total Submissions: 203.4K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#
class Solution(object):
    # solution 2: Your runtime beats 97.94 % of python submissions
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s)==0:
            return 0
        
        hs,ans=set(),0
        for ss in s:
            if ss in hs:
                hs.remove(ss)
                ans +=2
            else:
                hs.add(ss)
        if len(hs) >0:
            ans +=1
        return ans

    '''
    # Solution 1: Your runtime beats 22.57 % of python submissions
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s)==0:
            return 0
        
        cnt, ans = {}, 0
        for ss in s:
            cnt[ss] = cnt.get(ss,0) +1

        odd_great_one = False # if we have odd occurences greater than 1
        one = False # only single occurence of a character
        for k in cnt:
            if cnt[k] %2 == 0:  # if even occurence of a character
                ans += cnt[k] # increase by that amnt
            elif cnt[k] > 1: # else if odd ocurrence
                ans += cnt[k] - 1
                odd_great_one = True
            else: # else if single occurence, take it as elem  in the middle of the palindrome
                one = True

        if odd_great_one == True:
            ans +=1
        
        if one == True and odd_great_one == False:
            ans += 1

        return ans
    '''


