#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (34.72%)
# Likes:    3232
# Dislikes: 408
# Total Accepted:    409.7K
# Total Submissions: 1.2M
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers, return an array of all the unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 
# 
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 
# 
# You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
class Solution:

    # solution 2: k-sum
    # 283/283 cases passed (112 ms)
    # Your runtime beats 77.72 % of python3 submissions
    # Your memory usage beats 55.75 % of python3 submissions (14.4 MB)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums, target, k):
            result = []
            if not nums or nums[0]*k > target or nums[-1]*k < target:
                return result
            
            if k==2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                for _, set in enumerate(kSum(nums[i+1:], target-nums[i], k-1)):
                    result.append([nums[i]] + set)

            return result

        def twoSum(nums, target):
            result = []
            n = len(nums)
            start, end = 0, n-1
            while start < end:               
                if start > 0 and nums[start]==nums[start-1]:
                    start +=1
                    continue
                if end < n-1 and nums[end]== nums[end+1]:
                    end -= 1
                    continue
                
                two_sum = nums[start] + nums[end]
                if two_sum < target:
                    start +=1
                elif two_sum > target:
                    end -= 1
                else:
                    result.append([nums[start], nums[end]])
                    start += 1
                    end -= 1

            return result
        
        nums.sort()
        return kSum(nums, target, 4)
                
    '''
    # solution 1: two points - two sum
    def fourSum01(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        if not nums:
            return result

        n = len(nums)
        nums.sort()
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]: # skip the duplicate
                continue

            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]: # skip the duplicate
                    continue

                pairs = self.twoSum(nums, j+1,n-1,target - (nums[i]+nums[j]))

                for (c,d) in pairs:
                    result.append([nums[i],nums[j],c,d])
        
        return result
    
    def twoSum(self, nums, start, end, target):
        pairs = []
        while start < end:
            two_sum = nums[start] + nums[end]
            if two_sum==target:
                # skip the duplicate
                if not pairs or (nums[start], nums[end]) != pairs[-1]: 
                    pairs.append((nums[start], nums[end]))
                start +=1
                end -= 1
            elif two_sum < target:
                start +=1
            else:
                end -=1
        
        return pairs
    '''
            

        
# @lc code=end

