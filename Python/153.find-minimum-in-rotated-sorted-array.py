#
# @lc app=leetcode id=153 lang=python
#
# [153] Find Minimum in Rotated Sorted Array
#
class Solution(object):
    # Your runtime beats 60.93 % of python submissions
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==0:
            return -1

        n =len(nums)
        start,end = 0, n-1
        target = nums[n-1]
        while(start +1 <end):
            mid = start + (end-start)/2
            if nums[mid] < target:
                end = mid
            else:
                start = mid
        if nums[start]<nums[end]:
            return nums[start]
        else:
            return nums[end]
        

