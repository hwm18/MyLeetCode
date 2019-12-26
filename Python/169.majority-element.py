#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return -1
        
        # NOTICE that the majority element always exist in the array,so that the middle always is the answer
        return sorted(nums)[len(nums)//2]

    '''       
    def majorityElement(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return -1
        
        result = nums[0]
        count = 1
        for i in range(1, len(nums)):
            curr = nums[i]
            if count==0:
                result = curr
                count = 1
            else:          
                if curr == result:
                    count += 1
                else:
                    count -=1
        
        return result
    '''

# @lc code=end

