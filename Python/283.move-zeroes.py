#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
class Solution:
    # Solution 3: 这个版本可以保证最小的“写”次数。
    # steps: 1. 把不是0的数都写到数组前面部分；2. 数组后面部分全部置为0
    def moveZeroes(self, nums):
        if not nums:
            return
        
        left,right=0, 0
        n = len(nums)
        while right < n:
            if nums[right] !=0:
                if left != right:
                    nums[left] = nums[right]
                left += 1
            right += 1
        
        while left<n:
            if nums[left] != 0:
                nums[left] = 0
            left += 1


    '''
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
        


        # method 1: move all the not 0 to the front
        # Your runtime beats 83.3 % of python3 submissions
        n = len(nums)
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
    '''

    '''
    # 基于 swap 的版本，无法保证写次数最小。但比较好理解。
    # 21/21 cases passed (52 ms)
    # Your runtime beats 49.03 % of python3 submissions
    # Your memory usage beats 18.26 % of python3 submissions (15.5 MB)
    def moveZeroes(self, nums):
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
    '''

    

