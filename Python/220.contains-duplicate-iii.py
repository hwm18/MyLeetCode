#
# @lc app=leetcode id=220 lang=python
#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (19.68%)
# Likes:    643
# Dislikes: 603
# Total Accepted:    91.2K
# Total Submissions: 463.3K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
#
#
#
# Example 2:
#
#
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
#
#
#
# Example 3:
#
#
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
#
#
#
#
#
class Solution(object):
    # solution 2: Your runtime beats 78.29 % of python submissions
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # Write your code here
        if t < 0 or not nums:
            return False

        buckets = {}
        for i, v in enumerate(nums):
            # t == 0 is a special case where we only have to check the bucket
            # that v is in.
            bucketNum, offset = (v / t, 1) if t else (v, 0)
            for idx in xrange(bucketNum - offset, bucketNum + offset + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True

            buckets[bucketNum] = nums[i]
            if len(buckets) > k:
                # Remove the bucket which is too far away. Beware of zero t.
                del buckets[nums[i - k] / t if t else nums[i - k]]

        return False

    '''
    """
    The idea is like the bucket sort algorithm. Suppose we have consecutive buckets covering the range of nums with each bucket a width of (t+1). If there are two item with difference <= t, one of the two will happen:

    (1) the two in the same bucket
    (2) the two in neighbor buckets
    """

    # Your runtime beats 46.23 % of python submission
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums or t < 0:
            return False
        n = len(nums)
        d, w = {}, t + 1
        for i in range(n):
            m = nums[i] // w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k:
                del d[nums[i - k] // w]
        return False
    '''
