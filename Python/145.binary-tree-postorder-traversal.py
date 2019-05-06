#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        self.result = []
        self.postorder(root)
        return self.result
    
    def postorder(self, root):
        if not root:
            return
        
        self.postorder(root.left)
        self.postorder(root.right)
        self.result.append(root.val)

