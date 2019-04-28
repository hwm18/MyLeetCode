#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return 0
              
        ans = 0
        for x in nums:         
            if x-1 not in nums: 
                r = x + 1           
                while r in nums:
                    r += 1                   
                ans = max(ans, r -x)
        return ans
            
        '''
        # Your runtime beats 92.08 % of python3 submissions
        for x in nums:
            if x -1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                
                ans = max(ans, y -x)
        return ans
        '''


    '''
    Time Limit Exceeded  66/68#
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return 0
        
        n = len(nums)
        dic = {}
        for x in nums:
            dic[x] =1

        ans = 0
        for x in nums:
            lenn = 1
            if x in dic:
                del dic[x]
            
            l, r = x -1, x +1
            while l in dic:
                l -=1
                lenn +=1

            while r in dic:
                r += 1
                lenn += 1
            
            ans = max(ans, lenn)
        return ans
    '''
        

