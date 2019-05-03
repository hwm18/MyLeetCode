#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or k==0:
            return
        
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n-k-1)
        self.reverse(nums, n-k, n-1)
        self.reverse(nums, 0, n-1)
        
    def reverse(self, nums, start, end):
        if(start >= end):
            return
        
        while(start < end):
            t = nums[start]
            nums[start] = nums[end]
            nums[end] = t
            start +=1
            end -= 1

        

