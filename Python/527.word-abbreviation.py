#
# @lc app=leetcode id=527 lang=python
#
# [527] word-abbreviation
#
# https://www.lintcode.com/problem/word-abbreviation/description
# https://leetcode.com/problems/word-abbreviation/description/
#

# Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.
# Begin with the first character and then the number of characters abbreviated, which followed by the last character.
# If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
# If the abbreviation doesn't make the word shorter, then keep it as original.
# Both n and the length of each word will not exceed 400.
# The length of each word is greater than 1.
# The words consist of lowercase English letters only.
# The return answers should be in the same order as the original array.
# 
# Example 1:
# Input:
# ["like","god","internal","me","internet","interval","intension","face","intrusion"]
# Output:
# ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
# 
# Example 2:
# Input:
# ["where","there","is","beautiful","way"]
# Output:
# ["w3e","t3e","is","b7l","way"]
# 
# 
#
class Solution:
    """
    @param dict: an array of n distinct non-empty strings
    @return: an array of minimal possible abbreviations for every word
    """
    def wordsAbbreviation(self, dict):
        # write your code here
        if not dict or len(dict)==0:
            return []
            
        n = len(dict)
        prefix = [0] * n
        ans, mp = [], {}
        for i in range(n):
            prefix[i] = 1
            ans.append(self.getabbr(dict[i], 1))
            if ans[i] in mp:
                mp[ans[i]] = mp.get(ans[i]) + 1
            else:
                mp[ans[i]] = 1
            
        while True:
            unique = True
            for i in range(n):
                if mp[ans[i]] > 1:
                    prefix[i] +=1
                    ans[i] = self.getabbr(dict[i], prefix[i])
                    #mp[ans[i]] += 1
                    if ans[i] in mp:
                        mp[ans[i]] = mp.get(ans[i]) + 1
                    else:
                        mp[ans[i]] = 1
                    unique =False
            if unique == True:
                break
        
        return ans
        
    def getabbr(self, ss, idx):
        if idx >= len(ss) -2:
            return ss
        return ss[0: idx] + str(len(ss)-idx-1) + ss[-1]    
    
    
    
    
    
            




