#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
class Solution:
    # Your runtime beats 81.79 % of python3 submissions
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2 or not nums1:
            return
        
        l1,l2,idx=m-1,n-1,m+n-1
        while l1>=0 and l2>=0:
            if nums1[l1]>=nums2[l2]:
                nums1[idx] = nums1[l1]
                idx -=1
                l1 -=1
            else:
                nums1[idx] = nums2[l2]
                idx -=1
                l2 -=1

        while l2>=0:
            nums1[idx] = nums2[l2]
            idx -=1
            l2 -=1


           

