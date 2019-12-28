#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        # solution 1: recursion
        #return self.helper(root)
        # solution 2: use stack
        return self.useStackToInvert(root)
    
    # Solution 2: 用stack,模拟先序遍历
    # Your runtime beats 93.88 % of python3 submissions
    def useStackToInvert(self, root):
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                node.left,node.right = node.right,node.left
                stack += node.left, node.right
        return root

    # Solution 1: divid conque - Your runtime beats 82.34 % of python3 submissions
    def helper(self, root):
        if not root:
            return root
        
        root.right = self.helper(root.left)
        root.left = self.helper(root.right)
        return root

        
# @lc code=end

