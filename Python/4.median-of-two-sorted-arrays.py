#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (25.97%)
# Total Accepted:    411.9K
# Total Submissions: 1.6M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
#
# Example 2:
#
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
#
#
#
class Solution:
    import math

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        l = len(nums1) + len(nums2)
        if l % 2 == 0:
            return (
                self.findKth(nums1, 0, nums2, 0, l // 2)
                + self.findKth(nums1, 0, nums2, 0, l // 2 + 1)
            ) / 2.0
        else:
            return self.findKth(nums1, 0, nums2, 0, l // 2 + 1)

    def findKth(self, nums1, startIdx1, nums2, startIdx2, k):
        if startIdx1 >= len(nums1):
            return nums2[startIdx2 + k - 1]

        if startIdx2 >= len(nums2):
            return nums1[startIdx1 + k - 1]

        if k == 1:
            return min(nums1[startIdx1], nums2[startIdx2])

        halfKth1 = (
            nums1[startIdx1 + k // 2 - 1]
            if startIdx1 + k // 2 <= len(nums1)
            else None  # math.inf beats 80.76 %
        )
        halfKth2 = (
            nums2[startIdx2 + k // 2 - 1]
            if startIdx2 + k // 2 <= len(nums2)
            else None  # math.inf  beats 80.76 %
        )

        if halfKth2 is None or (
            halfKth1 is not None and halfKth1 < halfKth2
        ):  # beats 91.03 %
            # if halfKth1 < halfKth2:  80.76 %
            return self.findKth(nums1, startIdx1 + k // 2, nums2, startIdx2, k - k // 2)
        else:
            return self.findKth(nums1, startIdx1, nums2, startIdx2 + k // 2, k - k // 2)

