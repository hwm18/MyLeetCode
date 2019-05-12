#
# @lc app=leetcode id=944 lang=python
#
# [944] Search for a range
#
# https://leetcode.com/explore/learn/card/binary-search/135/template-iii/944/

# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
# 
#
class Solution(object):
     # twice binary search for left bound and right bound
     def searchRange(self, nums: List[int], target: int) -> List[int]:     
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or len(nums)==0:
            return [-1,-1]
        
        n=len(nums)
        l,r = -1,-1
        start, end = 0,n-1
        # find left bound
        while start + 1 < end:
            mid = start + (end - start) //2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            l = start
        elif nums[end] == target:
            l = end
        else:
            return [-1,-1]

        start, end = 0,n-1
        while start + 1 < end:
            mid = start + (end - start) //2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            r = end
        elif nums[start] == target:
            r = start
        else:
            return [-1,-1]

        return [l,r]





