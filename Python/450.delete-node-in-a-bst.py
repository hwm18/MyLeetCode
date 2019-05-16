#
# @lc app=leetcode id=450 lang=python
#
# [450] Delete Node in a BST
#
# https://leetcode.com/problems/delete-node-in-a-bst/description/
#
# algorithms
# Medium (39.88%)
# Likes:    875
# Dislikes: 55
# Total Accepted:    64.7K
# Total Submissions: 162.2K
# Testcase Example:  '[5,3,6,2,4,null,7]\n3'
#
# Given a root node reference of a BST and a key, delete the node with the
# given key in the BST. Return the root node reference (possibly updated) of
# the BST.
#
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node.
#
#
#
# Note: Time complexity should be O(height of tree).
#
# Example:
#
# root = [5,3,6,2,4,null,7]
# key = 3
#
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Given key to delete is 3. So we find the node with value 3 and delete it.
#
# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
#
# ⁠   5
# ⁠  / \
# ⁠ 4   6
# ⁠/     \
# 2       7
#
# Another valid answer is [5,2,6,null,4,null,7].
#
# ⁠   5
# ⁠  / \
# ⁠ 2   6
# ⁠  \   \
# ⁠   4   7
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
    # solution 2: Your runtime beats 99.92 % of python submissions
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val == key:
            if root.right:
                right_min = root.right
                while right_min.left:
                    right_min = right_min.left
                right_min.left = root.left
                return root.right
            else:
                return root.left

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

    '''
    # soluiton 1: Your runtime beats 99.05 % of python submissions
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        
        if root.val == key:
            if root.left:
                # Find the right most leaf of the left sub-tree
                left_right_most = root.left
                while left_right_most.right:
                    left_right_most = left_right_most.right
                # Attach right child to the right of that leaf
                left_right_most.right = root.right
                # Return left child instead of root, a.k.a delete root
                return root.left
            else:
                return root.right
        # If left or right child got deleted, the returned root is the child of the deleted node.
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root
    '''

