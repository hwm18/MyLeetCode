#
# @lc app=leetcode id=701 lang=python
#
# [701] Insert into a Binary Search Tree
#
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
#
# algorithms
# Medium (75.50%)
# Likes:    317
# Dislikes: 38
# Total Accepted:    42.2K
# Total Submissions: 55.9K
# Testcase Example:  '[4,2,7,1,3]\n5'
#
# Given the root node of a binary search tree (BST) and a value to be inserted
# into the tree, insert the value into the BST. Return the root node of the BST
# after the insertion. It is guaranteed that the new value does not exist in
# the original BST.
# 
# Note that there may exist multiple valid ways for the insertion, as long as
# the tree remains a BST after insertion. You can return any of them.
# 
# For example, 
# 
# 
# Given the tree:
# ⁠       4
# ⁠      / \
# ⁠     2   7
# ⁠    / \
# ⁠   1   3
# And the value to insert: 5
# 
# 
# You can return this binary search tree:
# 
# 
# ⁠        4
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   /
# ⁠   1   3 5
# 
# 
# This tree is also valid:
# 
# 
# ⁠        5
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   
# ⁠   1   3
# ⁠        \
# ⁠         4
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    # solution 3:  Your runtime beats 75.14 % of python submissions
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        if root.val<val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
    '''

    # solution 2: Your runtime beats 50 % of python submissions
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        newNode = TreeNode(val)
        if not root:
            return newNode
        curr, last = root,None
        while curr:
            last = curr
            if curr.val <val:
                curr = curr.right
            else:
                curr = curr.left
        if last:
            if last.val>val:
                last.left = newNode
            else:
                last.right = newNode
        return root

    '''
    # solution 1: Your runtime beats 75.14 % of python submissions
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        newNode = TreeNode(val)
        if not root:
            return newNode
        
        dummyNode = TreeNode(-1)
        dummyNode.left = root
        while root:
            if root.val<val:
                if root.right is None:
                    root.right = newNode
                    break
                else:
                    root=root.right               
            else:
                if root.left is None:
                    root.left = newNode
                    break
                else:
                    root = root.left
        return dummyNode.left
    '''
        

        

