#
# @lc app=leetcode id=161 lang=python3
#
# [161] One Edit Distance
#
# https://leetcode.com/problems/one-edit-distance/description/
#
# algorithms
# Medium (33.02%)
# Likes:    791
# Dislikes: 133
# Total Accepted:    132.1K
# Total Submissions: 399.9K
# Testcase Example:  '"ab"\n"acb"'
#
# Given two strings s and t, return true if they are both one edit distance
# apart, otherwise return false.
# 
# A string s is said to be one distance apart from a string t if you can:
# 
# 
# Insert exactly one character into s to get t.
# Delete exactly one character from s to get t.
# Replace exactly one character of s with a different character to get t.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
# 
# 
# Example 2:
# 
# 
# Input: s = "", t = ""
# Output: false
# Explanation: We cannot get t from s by only one step.
# 
# 
# Example 3:
# 
# 
# Input: s = "a", t = ""
# Output: true
# 
# 
# Example 4:
# 
# 
# Input: s = "", t = "A"
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 10^4
# 0 <= t.length <= 10^4
# s and t consist of lower-case letters, upper-case letters and/or digits.
# 
# 
#

# @lc code=start
class Solution:
    '''
    136/136 cases passed (20 ms)
    Your runtime beats 99.47 % of python3 submissions
    Your memory usage beats 91.99 % of python3 submissions (14.2 MB)
    '''
    '''
    def isOneEditDistance(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if(n>m):
            return self.isOneEditDistance(t, s)
        
        if m-n >1:
            return False

        diff = m -n
        i =0
        while(i<n and s[i]==t[i]):
            i+=1
        if(i==n):
            return diff > 0 # append
        if(diff==0):
            i+=1 # modify
        while(i<n and s[i]==t[i+diff]):  # insert
            i+=1
        return i==n
    '''

    '''
    136/136 cases passed (40 ms)
    Your runtime beats 21.06 % of python3 submissions
    Your memory usage beats 98.28 % of python3 submissions (14.1 MB)
    '''
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns = len(s)
        mt = len(t)

        # Ensure that s is shorter than t.
        if(ns>mt):
            return self.isOneEditDistance(t, s)
        
        # The strings are NOT one edit away distance  
        # if the length diff is more than 1.
        if mt-ns >1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                # if strings have the same length
                if ns == mt:
                    return s[i+1:] == t[i+1:]
                else: # if strings have different lengths
                    return s[i:] == t[i+1:]
        
        # If there is no diffs on ns distance
        # the strings are one edit away only if
        # t has one more character. 
        return ns+1==mt


        
# @lc code=end

