#
# @lc app=leetcode id=154 lang=python
#
# [154] Find Minimum in Rotated Sorted Array II
#
class Solution(object):
    # Your runtime beats 54.67 % of python submissions
    def findMin(self, nums):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid if nums[end] != nums[mid] else end - 1
                
        if nums[start] < nums[end]:
            return nums[start]
        return nums[end]

    """
    # Your runtime beats 47.94 % of python submissions
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi -lo) / 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid if nums[hi] != nums[mid] else hi - 1
        return nums[lo]
        """

    '''
    # Your runtime beats 47.11 % of python submissions
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==0:
            return  -1
        n = len(nums)
        ans = 1<<31
        for i in nums:
            if i < ans:
                ans = i
        return ans
    '''

