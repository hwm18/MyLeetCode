#
# @lc app=leetcode id=438 lang=python
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (36.92%)
# Total Accepted:    116.9K
# Total Submissions: 316.2K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
#
class Solution(object):
    # Your runtime beats 63.32 % of python submissions
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ls, lp = len(s), len(p)
        if lp > ls:
            return []

        det = [0] * 30
        for i in range(lp):
            det[ord(p[i]) - ord('a')] -= 1
            det[ord(s[i]) - ord('a')] += 1

        ans, abs_sum = [], 0
        for item in det:
            abs_sum += abs(item)
        
        if abs_sum == 0:
            ans.append(0)
        
        i = lp
        while(i< ls):
            r, l = s[i], s[i-lp]
            abs_sum = abs_sum - abs(det[ord(r) - ord('a')]) - abs(det[ord(l) - ord('a')])
            det[ord(r) - ord('a')] += 1
            det[ord(l) - ord('a')] -= 1

            abs_sum = abs_sum + abs(det[ord(r) - ord('a')]) + abs(det[ord(l) - ord('a')])
            if abs_sum == 0:
                ans.append(i - lp +1)
            
            i+=1
        
        return ans


            

            
        #while(i+lp-1 < ls):
            # if self.isAnagrams(s[i:i+lp], p):
            #     result.append(i)
            # i += 1

        return result


    def isAnagrams(self, s, t):
        count_s = [0] * 256
        for ss in s:
            count_s[ord(ss)] += 1
        
        for tt in t:
            count_s[ord(tt)] -= 1

        for v in count_s:
            if v != 0:
                return False
        return True
        

