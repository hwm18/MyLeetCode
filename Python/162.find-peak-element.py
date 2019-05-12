#
# @lc app=leetcode id=162 lang=python
#
# [162] Find Peak Element
#
class Solution(object):
    # Your runtime beats 52.41 % of python submissions
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==0:
            return -1
        
        start,end =0,len(nums)-1
        while start + 1< end:
            mid = start + (end - start)/2

            if nums[mid] < nums[mid+1]:
                start = mid
            else:
                end = mid
        
        if nums[start]>nums[end]:
            return start
        
        return end
        

