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
    # solution 2: Your runtime beats 97.43 % of python3 submissions
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        traversal, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    traversal.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return traversal

            
    '''
    # Method 1: Your runtime beats 17.47 % of python3 submissions
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
    '''

