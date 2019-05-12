#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
class Solution:
    # Your runtime beats 94.19 % of python3 submissions
    def search(self, nums: List[int], target: int) -> int:
        if not nums or len(nums)==0:
            return -1
        n = len(nums)
        start, end = 0, n-1
        while(start +1 < end):
            mid = start + (end - start) // 2

            #Your runtime beats 99.08 % of python3 submissions
            if nums[mid] == target:  
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
        
        

