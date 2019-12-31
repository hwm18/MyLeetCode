#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    # This is a dutch partitioning problem. We are classifying the array into four groups: 
    # red, white, unclassified, and blue. Initially we group all elements into unclassified. 
    # We iterate from the beginning as long as the white pointer is less than the blue pointer.

    # If the white pointer is red (nums[white] == 0), we swap with the red pointer and move both
    # white and red pointer forward. If the pointer is white (nums[white] == 1), the element is 
    # already in correct place, so we don’t have to swap, just move the white pointer forward. 
    # If the white pointer is blue, we swap with the latest unclassified element.
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

