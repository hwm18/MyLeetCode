#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    '''
    Accepted
    62/62 cases passed (48 ms)
    Your runtime beats 86.62 % of python3 submissions
    Your memory usage beats 33.08 % of python3 submissions (14.6 MB)
    '''
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums or len(nums)==0:
            return 0
        
        n = len(nums)
        start, end = 0, n-1
        while start <= end:  # <=
            mid = start + (end -start) //2
            
            if nums[mid]==target:
                return mid
            
            if nums[mid] < target:
                start = mid + 1  # mid + 1
            else:
                end = mid -1     # mid - 1
        
        return start


    '''
    Accepted
    62/62 cases passed (44 ms)
    Your runtime beats 95.49 % of python3 submissions
    Your memory usage beats 65.68 % of python3 submissions (14.5 MB)
    '''
    '''
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums or len(nums)==0:
            return 0
        
        n = len(nums)
        start, end = 0, n-1
        while start +1 < end:
            mid = start + (end -start) //2
            
            if nums[mid]==target:
                return mid
            
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        
        if nums[start]>=target:
            return start
        if nums[end] >= target:
            return end
        return end+1
    '''

        
# @lc code=end

