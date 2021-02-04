#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (40.89%)
# Likes:    1200
# Dislikes: 105
# Total Accepted:    316.9K
# Total Submissions: 775K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the depth of the two subtrees of every node never
# differ by more than 1.
# 
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# Return false.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Your runtime beats 79.85 % of python submissions
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        # buttom to top
        return self.helper(root) !=-1
        
        # recursion: top to buttom
        #return abs(self.maxDepth(root.left)-self.maxDepth(root.right)) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def helper(self, root):
        if not root:
            return 0
        l = self.helper(root.left)
        if l == -1:
            return -1        
        r = self.helper(root.right)
        if r == -1:
            return -1
        if abs(l -r)>1:
            return -1

        return max(l,r)+1
    
    def maxDepth(self, root):
        if root == None:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

