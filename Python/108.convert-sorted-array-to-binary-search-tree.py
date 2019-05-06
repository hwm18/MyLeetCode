#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Method 1: Your runtime beats 88.22 % of python3 submissions
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        return self.helper(nums,0, len(nums)-1)

    def helper(self, nums, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(nums[start])
        
        mid = start + (end -start)//2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums,start,mid-1)
        root.right = self.helper(nums, mid+1,end)
        return root
        

