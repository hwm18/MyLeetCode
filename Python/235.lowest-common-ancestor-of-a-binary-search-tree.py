#
# @lc app=leetcode id=235 lang=python
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Easy (44.50%)
# Likes:    999
# Dislikes: 79
# Total Accepted:    277.9K
# Total Submissions: 624.5K
# Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n2\n8'
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
# two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
#
#
#
# Example 1:
#
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
#
#
# Example 2:
#
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
# of itself according to the LCA definition.
#
#
#
#
# Note:
#
#
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.
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
    # solution 1: Your runtime beats 99.33 % of python submissions
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or p is None or q is None:
            return None

        if p.val > q.val:
            p, q = q, p
        if root.val == p.val or root.val == q.val:
            return root

        if root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root

    '''
    # solution 2: Your runtime beats 8.85 % of python submissions
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is None:
            return right
        elif right is None:
            return left
        return root
    '''

