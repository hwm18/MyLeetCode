#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (37.31%)
# Likes:    737
# Dislikes: 209
# Total Accepted:    203K
# Total Submissions: 543.9K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# Example 1:
# 
# 
# Input: s = "egg", t = "add"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "foo", t = "bar"
# Output: false
# 
# Example 3:
# 
# 
# Input: s = "paper", t = "title"
# Output: true
# 
# Note:
# You may assume both s and t have the same length.
# 
#
class Solution(object):
    # solution 2:  Your runtime beats 45.74 % of python submissions
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1,d2=[0]*256, [0]*256
        for i in range(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i +1
            d2[ord(t[i])] = i +1
        return True

    '''  
    # solution 1: Your runtime beats 9.76 % of python submissions
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not s:
            return True
        if not s or not s:
            return False
        if len(s) != len(t):
            return False

        cnt_s,cnt_t={},{}
        for i,val in enumerate(s):
            cnt_s[val] = cnt_s.get(val, []) + [i]

        for i,val in enumerate(t):
            cnt_t[val] = cnt_t.get(val, []) + [i]

        if len(cnt_s) != len(cnt_t):
            return False
        return sorted(cnt_s.values()) == sorted(cnt_t.values())
    '''
        
    ''' other solutions
    def isIsomorphic2(self, s, t):
        d1, d2 = [[] for _ in xrange(256)], [[] for _ in xrange(256)]
        for i, val in enumerate(s):
            d1[ord(val)].append(i)
        for i, val in enumerate(t):
            d2[ord(val)].append(i)
        return sorted(d1) == sorted(d2)
    
    def isIsomorphic3(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        
    def isIsomorphic4(self, s, t): 
        return [s.find(i) for i in s] == [t.find(j) for j in t]
        
    def isIsomorphic5(self, s, t):
        return map(s.find, s) == map(t.find, t)

    '''


        

