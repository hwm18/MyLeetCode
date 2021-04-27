#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (53.64%)
# Likes:    2523
# Dislikes: 403
# Total Accepted:    284.9K
# Total Submissions: 525.7K
# Testcase Example:  '[2,2,3,2]'
#
# Given an integer array nums where every element appears three times except
# for one, which appears exactly once. Find the single element and return
# it.
# 
# 
# Example 1:
# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# Each element in nums appears exactly three times except for one element which
# appears once.
# 
# 
# 
# Follow up: Your algorithm should have a linear runtime complexity. Could you
# implement it without using extra memory?
# 
#

# @lc code=start
class Solution:
    # solutin 1:
    # 14/14 cases passed (60 ms)
    # Your runtime beats 47.32 % of python3 submissions
    # Your memory usage beats 71.46 % of python3 submissions (15.8 MB)
    def singleNumber(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return nums

        ones,twos,threes=0,0,0
        for i in range(len(nums)):
            num = nums[i]
            twos ^= ones & num
            ones ^= num 
            threes = ~(ones & twos)
            twos &= threes
            ones &= threes
            
        return ones

    '''
    # solutin 2:
    # 14/14 cases passed (52 ms)
    # Your runtime beats 88.21 % of python3 submissions
    # Your memory usage beats 58 % of python3 submissions (16 MB)
    def singleNumber(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return nums

        map = {}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            map[num] = map.get(num, 0) +1
        
        for k,v in map.items():
            if v is not 3:
                return k
        
        return None
    '''

        
# @lc code=end

