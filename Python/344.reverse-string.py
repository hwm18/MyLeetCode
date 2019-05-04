#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
class Solution:
    # Your runtime beats 23.64 % of python3 submissions
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s or len(s)==0:
            return
        l,r =0,len(s)-1
        while l<r:
            s[l],s[r] = s[r],s[l]
            l +=1
            r -= 1

        # method 1: Your runtime beats 76.03 % of python3 submissions
        # s.reverse()

