#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    '''
   Accepted
    88/88 cases passed (76 ms)
    Your runtime beats 99.49 % of python3 submissions
    Your memory usage beats 71.24 % of python3 submissions (15.1 MB)
    '''
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) == 0:
            return [-1,-1]

        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left +1 < right:
                mid = left + (right - left) // 2
                if x > A[mid]:
                    left = mid
                else:
                    right = mid

            if (A[left] == target):
                return left
            if (A[right] == target):
                return right
            return -1

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left + 1 < right:
                mid = left + (right - left) // 2
                if x < A[mid]:
                    right = mid
                else:
                    left = mid

            if(A[right] == target):
                return right
            if(A[left] == target):
                return left
            return -1

        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return [left, right]

    '''
    Accepted
    88/88 cases passed (88 ms)
    Your runtime beats 81.12 % of python3 submissions
    Your memory usage beats 68.78 % of python3 submissions (15.1 MB)
    '''
    '''
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) ==0:
            return [-1,-1]

        n = len(nums)
        start, end = 0, n-1
        left, right = -1, -1
        # find left
        while (start + 1 < end):
            mid = start + (end - start) // 2
            
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        
        if nums[start] == target:
            left = start
        elif nums[end] == target:
            left = end
        else:
            return [-1,-1]
        
        # find right
        start, end = 0, n-1
        while (start + 1 < end):
            mid = start + (end - start) // 2
            
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        
        if nums[end] == target:
            right = end
        elif nums[start] == target:
            right = start
        else:
            return [-1,-1]

        return [left, right]
    '''
        
# @lc code=end

