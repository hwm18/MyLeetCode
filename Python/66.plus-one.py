#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
class Solution:
    # soluiton 2: Your runtime beats 60 % of python3 submissions
    def plusOne(self, digits: List[int]) -> List[int]:
        num, n = 0, len(digits)
        for i in range(n):
            num += digits[i] * pow(10, (n-1-i))
        return [int(i) for i in str(num+1)]

    '''
    # soluiton 1:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits or len(digits)==0:
            return [1]
        
        n = len(digits)        
        i,p = n -1,1
        result = []
        while i >=0 and p>0:
            curr = digits[i]+p            
            digits[i] = curr%10
            i -=1
            p = curr//10
            
        if p>0:
            digits.insert(0,p)
            
        return digits
    ''' 

    '''
        if str(digits[-1]) in '012345678':
            digits[-1] +=1
            return digits
        
        i = len(digits)-2
        r = 1
        digits[-1] = 0
        while i>=0 and r>0:
            s = (digits[i] +r)
            digits[i] = s%10
            r = s//10
            i -=1
        if r >0:
            digits.insert(0,r)
        return digits
    '''




        

