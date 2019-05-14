#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
class Solution:
    # Solution 1: use set operation in python, one-line solution
    # √ Your runtime beats 99.09 % of python3 submissions
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        s1, s2=set(nums1), set(nums2)
        result = []
        for s in s1:
            if s in s2:
                result.append(s)
        return result
    """

