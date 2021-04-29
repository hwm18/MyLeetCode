#
# @lc app=leetcode id=360 lang=python3
#
# [360] Sort Transformed Array
#
# https://leetcode.com/problems/sort-transformed-array/description/
#
# algorithms
# Medium (49.56%)
# Likes:    408
# Dislikes: 115
# Total Accepted:    39.9K
# Total Submissions: 79.8K
# Testcase Example:  '[-4,-2,2,4]\n1\n3\n5'
#
# Given a sorted integer array nums and three integers a, b and c, apply a
# quadratic function of the form f(x) = ax^2 + bx + c to each element nums[i]
# in the array, and return the array in a sorted order.
# 
# 
# Example 1:
# Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# Output: [3,9,15,33]
# Example 2:
# Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# Output: [-23,-5,1,7]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 200
# -100 <= nums[i], a, b, c <= 100
# nums is sorted in ascending order.
# 
# 
# 
# Follow up: Could you solve it in O(n) time?
# 
#

# @lc code=start
class Solution:
    # 110/110 cases passed (36 ms)
    # Your runtime beats 91.62 % of python3 submissions
    # Your memory usage beats 49.21 % of python3 submissions (14.4 MB)
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        results = [a * x*x + b*x+c for x in nums]
        ans = []
        left,right = 0, len(nums)-1

        while left <=right:
            if (a > 0) ^ (results[left] < results[right]):
                ans.append(results[left])
                left += 1
            else:
                ans.append(results[right])
                right -= 1
        
        return ans if a<=0 else ans[::-1]
        
# @lc code=end

