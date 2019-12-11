#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums)==0:
            return

        #red, white, blue =0,1,2
        n = len(nums)
        red, white, blue =0,0,n-1
        while white<=blue:
            if nums[white] ==0:
                nums[red],nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 2:
                nums[white],nums[blue] = nums[blue], nums[white]
                blue -= 1
            else:
                white += 1
        

# [2,0,2,1,1,0]
        
# @lc code=end

