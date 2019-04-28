#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        
        l1, l2 = len(s1), len(s2)
        if(l1 != l2):
            return False
        
        if s1 == s2:
            return True
        
        if sorted(list(s1)) != sorted(list(s2)):
            return False
        
        for i in range(1, l1):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            if self.isScramble(s1[:i],s2[l1-i:]) and self.isScramble(s1[i:],s2[:l1-i]):
                return True
        return False
        

