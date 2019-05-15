#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (23.93%)
# Likes:    3693
# Dislikes: 402
# Total Accepted:    540.9K
# Total Submissions: 2.3M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#
class Solution(object):
    # Your runtime beats 75.82 % of python submissions
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) == 0:
            return []
        ans, n = [], len(nums)
        nums.sort()
        for i in range(n - 1):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            start, end = i + 1, n - 1
            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if s < 0:
                    start += 1
                elif s > 0:
                    end -= 1
                else:
                    ans.append((nums[i], nums[start], nums[end]))
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1

                    start += 1
                    end -= 1
        return ans

