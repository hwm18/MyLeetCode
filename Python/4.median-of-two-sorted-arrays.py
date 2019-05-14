#
# @lc app=leetcode id=4 lang=python
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
    # Solution 1: Your runtime beats 44.14 % of python submissions
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   
    
    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]
        
        # when k is bigger than the sum of a and b's median indices 
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

    '''
    # Solution 1:
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
        '''

