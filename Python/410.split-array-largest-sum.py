#
# @lc app=leetcode id=410 lang=python
#
# [410] Split Array Largest Sum
#
# https://leetcode.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (42.35%)
# Likes:    686
# Dislikes: 39
# Total Accepted:    40.6K
# Total Submissions: 95.8K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# Given an array which consists of non-negative integers and an integer m, you
# can split the array into m non-empty continuous subarrays. Write an algorithm
# to minimize the largest sum among these m subarrays.
# 
# 
# Note:
# If n is the length of array, assume the following constraints are satisfied:
# 
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# 
# 
# 
# Examples: 
# 
# Input:
# nums = [7,2,5,10,8]
# m = 2
# 
# Output:
# 18
# 
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
# 
# 
#
class Solution(object):
    # Your runtime beats 99.87 % of python submissions
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def valid(mid):
            cnt,curr=0,0
            for num in nums:
                curr +=num
                if curr>mid:
                    cnt +=1
                    if cnt >= m:
                        return False
                    curr = num
            return True
        
        start,end = max(nums),sum(nums)
        if m==1:
            return end

        while start +1<end:
            mid = start + (end - start)//2
            if valid(mid):
                end = mid
            else:
                start = mid
        # start +1 == end
        if valid(start):
            return start
        return end

