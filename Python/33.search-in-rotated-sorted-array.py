#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#
class Solution(object):
    '''
    Accepted
    195/195 cases passed (32 ms)
    Your runtime beats 63.74 % of python submissions
    Your memory usage beats 93.31 % of python submissions (12.9 MB)
    '''
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        start, end = 0,len(nums)-1
        while(start + 1 < end):
            mid = start + (end - start) // 2

            if nums[start] <= nums[mid]:
                if nums[start]<= target <= nums[mid]:
                    end = mid
                else:
                    start = mid 
            else:
                if nums[mid]<= target <= nums[end]:
                    start = mid
                else:
                    end = mid
        
        if nums[start]==target:
            return start
        if nums[end] == target:
            return end

        return -1
    
    '''
    # Your runtime beats 95.84 % of python submissions
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums)==0:
            return -1
        n = len(nums)
        start, end = 0,n-1
        while(start + 1 < end):
            mid = start + (end - start)/2
            if target == nums[mid]:
                return mid

            if nums[start] < nums[mid]:
                if nums[start]<=target and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid]<=target and target <= nums[end]:
                    start = mid
                else:
                    end = mid
            
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
    '''


