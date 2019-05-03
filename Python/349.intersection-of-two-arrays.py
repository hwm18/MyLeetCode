#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        s1, s2=set(nums1), set(nums2)
        result = []
        for s in s1:
            if s in s2:
                result.append(s)
        return result
        

