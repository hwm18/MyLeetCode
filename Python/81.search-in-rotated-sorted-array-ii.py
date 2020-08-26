#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    '''
    Accepted
    275/275 cases passed (56 ms)
    Your runtime beats 72.42 % of python3 submissions
    Your memory usage beats 25.71 % of python3 submissions (14.3 MB)
    '''
    def search(self, nums: List[int], target: int) -> bool:
        if not nums or len(nums)==0:
            return False
        
        n = len(nums)
        start, end = 0, n-1
        while start <=end:
            mid = start + (end - start) //2
            if nums[mid]==target:
                return True
            
            if nums[start]<nums[mid]:
                if nums[start]<= target and target<nums[mid]:
                    end = mid -1
                else:
                    start = mid + 1
            elif nums[start]> nums[mid]:
                if nums[mid]< target and target<=nums[end]:
                    start = mid + 1
                else:
                    end = mid -1
            else:
                start += 1
        
        return False

        
# @lc code=end

