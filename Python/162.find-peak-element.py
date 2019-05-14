#
# @lc app=leetcode id=162 lang=python
#
# [162] Find Peak Element
#
class Solution(object):
    '''
    # solution 2:  Your runtime beats 49.39 % of python submissions
    Conditions:
     1. array length is 1  -> return the only index 
     2. array length is 2  -> return the bigger number's index 
     3. array length is bigger than 2 -> 
           (1) find mid, compare it with its left and right neighbors  
           (2) return mid if nums[mid] greater than both neighbors
           (3) take the right half array if nums[mid] smaller than right neighbor
           (4) otherwise, take the left half
    '''
    def findPeakElement(self, nums):
        start = 0
        end = len(nums)-1

        # handle condition 3
        while start +1 < end:
            mid = start + (end-start)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
                
            if nums[mid] < nums[mid+1]:
                start = mid+1
            else:
                end = mid-1
                
        #handle condition 1 and 2
        return start if nums[start] >= nums[end] else end

    '''
    # Your runtime beats 52.41 % of python submissions
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==0:
            return -1
        
        n = len(nums)
        if n ==1:
            return 0
        if n ==2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        start,end =0,len(nums)-1 # between
        while start + 1< end:
            mid = start + (end - start)/2
            if nums[mid] < nums[mid+1]:
                start = mid
            else:
                end = mid
        
        if nums[start]>nums[end]:
            return start
        
        return end
    '''
        

