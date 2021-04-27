#
# @lc app=leetcode id=153 lang=python
#
# [153] Find Minimum in Rotated Sorted Array
#
class Solution(object):
    '''
    Accepted
    146/146 cases passed (32 ms)
    Your runtime beats 60.9 % of python submissions
    Your memory usage beats 93.78 % of python submissions (12.9 MB)
    '''
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

        # start +1 = end
        return nums[start] if nums[start] < nums[end] else nums[end]
        #return min(nums[start], nums[end])
        

