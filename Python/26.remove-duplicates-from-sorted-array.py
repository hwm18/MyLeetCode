#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        idx =-1
        for item in nums:
            if(idx == -1 or item != nums[idx]):
                idx +=1
                nums[idx] = item
        
        return idx + 1

        

