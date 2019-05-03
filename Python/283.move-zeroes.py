#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums)==0:
            return
        # method 2:  two points: when found 0, swap it with the nearest right not 0 item
        n = len(nums)
        for left in range(n):
            if nums[left] ==0:
                right = left +1
                while(right < n and nums[right]==0):
                    right +=1
                if right >= n:
                    break
                
                nums[left],nums[right] = nums[right], nums[left]
        


        '''
        # method 1: move all the not 0 to the front
        # Your runtime beats 83.3 % of python3 submissions
        n = len(nums)
        zeroIdx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zeroIdx],nums[i], zeroIdx = nums[i],nums[zeroIdx], zeroIdx +1
        '''

    

