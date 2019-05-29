#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
class Solution:
    # Your runtime beats 91.73 % of python3 submissions
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums)==0:
            return False
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False

        # count = {}
        # for n in nums:
        #     if n not in count:
        #         count[n] = 1
        #     else:
        #         return True
        # return False
        
        '''
        nums.sort()
        pre = -1
        for n in nums:
            if pre != -1 and nums[pre]==n:
                return True
            pre +=1

        return False
        '''
        

