#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#
class Solution:
    # method 3: Your runtime beats 99.17 % of python3 submissions
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        if n==1:
            return True
            
        return (n%3==0 and self.isPowerOfThree(n/3))

    '''
    # Mehtod 2: Your runtime beats 99.57 % of python3 submissions
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        num = 1
        while num <= n:
            if num == n:
                return True
            num *=3
        return False
    '''
    '''
    # method 1: Your runtime beats 99.45 % of python3 submissions
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        
        while n%3==0:
            n /=3
        return n==1
    '''
        

