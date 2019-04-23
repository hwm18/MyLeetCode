#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (30.34%)
# Total Accepted:    226.3K
# Total Submissions: 744.1K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# Example:
# 
# 
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# 
# 
# Note:
# 
# 
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
# 
# Your runtime beats 64.64 % of python3 submissions
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t)==0:
            return ''
        
        countS = [0] * 256
        countT = [0] * 256
        K = 0

        for tt in t:
            countT[ord(tt)] += 1
            if countT[ord(tt)] == 1:
                K += 1

        l,r, C=0,0,0
        ansl, ansr = -1,-1
        for l in range(len(s)):
            while r < len(s) and C < K:
                countS[ord(s[r])] +=1
                if(countS[ord(s[r])] == countT[ord(s[r])]):
                    C +=1
                r +=1
            
            if K==C:
                if ansl ==-1 or r -l < ansr - ansl:
                    ansl = l
                    ansr = r
                
            countS[ord(s[l])] -= 1
            if(countS[ord(s[l])] == countT[ord(s[l])] -1):
                C -= 1

        if ansl == -1:
            return ''

        return s[ansl: ansr]




        

