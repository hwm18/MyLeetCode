#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
class Solution:
    # Your runtime beats 9.08 % of python3 submissions
    def firstUniqChar(self, s: str) -> int:
        if not s or len(s)==0:
            return -1
        
        cnt, e2idx = {},[0]*256
        for i in range(len(s)):
            c = ord(s[i])
            e2idx[c] =i
            cnt[c] = cnt.get(c,0) +1
        
        for c in s:
            if cnt[ord(c)] ==1:
                return e2idx[ord(c)]
            
        return -1

