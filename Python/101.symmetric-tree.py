#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #   √ Your runtime beats 99.21 % of python3 submissions
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        if left.val != right.val:
            return False
        
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)
        


