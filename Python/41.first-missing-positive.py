#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    # solution 3: O(nlgn)
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return 1

        nums.sort()
        result = 1
        for num in nums:
            if num == result:
                result += 1
        return result
        
    '''
    # solution 2: O(n)
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return 1
        
        n = len(nums)
        for i in range(n):            
            while 0<=nums[i] -1<n and nums[nums[i] -1] != nums[i]:
                temp = nums[i] -1
                nums[temp], nums[i]=nums[i],nums[temp]
        
        for i in range(n):
            if nums[i] !=i+1:
                return i+1
        return n+1
    '''

    '''
    # solution 1: O(n*2)
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return 1
        
        n = len(nums)
        for i in range(1, n+1):
            if i not in nums:
                return i 
        return n+1
    '''
# @lc code=end

