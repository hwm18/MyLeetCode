#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        result.append(root.val)
        
        for item in left:
            if item:
                result.append(item)
        for item in right:
            if item:
                result.append(item)
        return result


    '''
    # Method 2: Your runtime beats 84.45 % of python3 submissions
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, result = [],[]
        stack.append(root)
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
        return result

    '''

    '''
    # Method 1: Your runtime beats 84.45 % of python3 submissions
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        self.result = []
        self.helper(root)
        return self.result
    
    def helper(self, root):
        if not root:
            return

        self.result.append(root.val)
        self.helper(root.left)
        self.helper(root.right)
    '''


