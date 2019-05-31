#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
class Solution:
    # solution 2:  Your runtime beats 80.36 % of python3 submissions
    def firstUniqChar(self, s: str) -> int:
        if not s or len(s)==0:
            return -1
        
        d, q={},[]
        for i in range(len(s)-1, -1,-1):
            c = s[i]
            if c not in d:
                d[c] = i
                q.append(i)
            else:
                if d[c] != -1:
                    q.remove(d[c])
                    d[c] = -1
        if not q:
            return -1
        return q[-1]


    '''
    # solution 1: Your runtime beats 9.08 % of python3 submissions
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
    '''

