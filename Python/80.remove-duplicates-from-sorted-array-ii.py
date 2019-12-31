#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    # Skip the middle elements of the duplicates and rearrange the array.

    # Your runtime beats 99.31 % of python3 submissions
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     if not nums or len(nums)<3:
    #         return len(nums)
        
    #     slow,fast = 1, 1
    #     n = len(nums)
    #     while fast<n-1:
    #         if nums[fast -1] != nums[fast +1]:
    #             nums[slow] = nums[fast]
    #             slow += 1
    #         fast += 1
    #     nums[slow] = nums[-1]
           
    #     return slow +1

    # Your runtime beats 90.27 % of python3 submissions
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums)<3:
            return len(nums)

        pos =1
        for i in range(1, len(nums)-1):
            if nums[i-1] != nums[i+1]:
                nums[pos] = nums[i]
                pos += 1
        
        nums[pos] = nums[-1]
        return pos+1



    # The idea was pretty like solve remove-duplicates-from-sorted-array as below:
    # def removeDuplicates(self, nums):
    #         pos = 0
    #         for i in range(0, len(nums)):
    #             if i == 0 or nums[i-1] != nums[i]:
    #                 nums[pos] = nums[i]
    #                 pos += 1
    #         return pos

        
# @lc code=end

