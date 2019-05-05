#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
class Solution:
    # Method 3 Your runtime beats 25.14 % of python3 submissions
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs)==0:
            return ""
        pre, i = strs[0],1
        while(i<len(strs)):
            while(strs[i].find(pre) !=0):
                pre = pre[:len(pre)-1]
            i+=1
        return pre

    '''
    # Method 2: Your runtime beats 25.14 % of python3 submissions
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs)==0:
            return ""
        shortest = min(strs,key=len)
        for idx, ch in enumerate(shortest):
            for other in strs:
                if ch !=other[idx]:
                    return shortest[:idx]
        return shortest
    
    # Method 1: Your runtime beats 73.92 % of python3 submissions
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs)==0:
            return ""
        n = len(strs)
        if n ==1:
            return strs[0]
        
        first = strs[0]
        l1, idx= len(first),0
        result= ''
        for c in first:
            i=1
            while i<n:
                if idx >= len(strs[i]):
                    return result
                if strs[i][idx] != c:
                    return result
                i+=1

            result +=c
            idx +=1
            
        return result
        '''
        

