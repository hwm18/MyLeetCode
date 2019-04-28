#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if( not root):
            return root
        self.sum = 0
        self.dfs(root)
        return root
    
    
    def dfs(self, curr):
        if not curr:
            return
        
        self.dfs(curr.right)
        self.sum += curr.val
        curr.val = self.sum
        self.dfs(curr.left)



