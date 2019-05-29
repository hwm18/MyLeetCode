#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
class Solution:
    # soluiton 2: use hashmap. Your runtime beats 93.52 % of python3 submissions
    def singleNumber(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return -1
        
        d = {}
        for n in nums:
            cnt = d.get(n,0)+1
            d[n] = cnt
        for k,v in d.items():
            if v ==1:
                return k
        

    '''    
    # solution 1: use XOR operation: a^a=0  0^a=a
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^=n
        return result
    '''
        
    ''' other soluitons
    def singleNumber3(self, nums):
        return 2*sum(set(nums))-sum(nums)
    
    def singleNumber4(self, nums):
        return reduce(lambda x, y: x ^ y, nums)
        
    def singleNumber(self, nums):
        return reduce(operator.xor, nums)

    '''

