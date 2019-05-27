#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (39.09%)
# Likes:    947
# Dislikes: 188
# Total Accepted:    302.3K
# Total Submissions: 773.3K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#
class Solution(object):
    '''
    # soultion 1: Your runtime beats 83.11 % of python submissions
    def addBinary(self, a, b):
            if len(a)==0: return b
            if len(b)==0: return a
            if a[-1] == '1' and b[-1] == '1':
                return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
            if a[-1] == '0' and b[-1] == '0':
                return self.addBinary(a[0:-1],b[0:-1])+'0'
            else:
                return self.addBinary(a[0:-1],b[0:-1])+'1'
    '''

    # soluiton 2: Your runtime beats 83.11 % of python submissions
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        if not b:
            return a

        ans = ''
        m,n=len(a)-1,len(b)-1
        r,s=0,0
        while(m>=0 or n>=0):
            aa,bb =0,0
            if m>=0:
                aa = int(a[m])
                m-=1
            if n>=0:
                bb = int(b[n])
                n -=1

            s = r+ aa+bb
            r = s // 2
            if s%2 == 0:
                ans = '0' + ans
            else:
                ans = '1' + ans

        if r>0:
            ans ='1' + ans
        return ans
        
         
            
       
             
            

        

