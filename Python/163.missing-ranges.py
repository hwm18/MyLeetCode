#
# @lc app=leetcode id=100 lang=python
#
# [163] Missing Ranges
#
# https://www.lintcode.com/problem/missing-ranges/description
#

#
# Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
# Example 1
# Input:
# nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99
# Output:
# ["2", "4->49", "51->74", "76->99"]
# Explanation:
# in range[0,99], the missing range includes:range[2,2],range[4,49],range[51,74] and range[76,99]

# Example 2
# Input:
# nums = [0, 1, 2, 3, 7], lower = 0 and upper = 7
# Output:
# ["4->6"]
# Explanation:
# in range[0,7],the missing range include range[4,6]

# Your submission beats 34.43% Submissions!
class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        result = []
        if(not nums or len(nums) == 0):
            result.append(self.helper(lower, upper))
            return result
        
        pre_point = lower -1
        for point in nums:
            if pre_point != point and pre_point+1 != point:
                result.append(self.helper(pre_point+1, point-1))
           
            pre_point = point
        
        if nums[-1] < upper:
            result.append(self.helper(nums[-1] + 1, upper))
                       
        return result
            
    def helper(self, left_point, right_point):
        if left_point == right_point:
            return str(left_point)
        else:
            return str(left_point) + "->" + str(right_point) 
            

        

