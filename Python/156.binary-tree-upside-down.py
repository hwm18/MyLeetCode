#
# @lc app=leetcode id=156 lang=python3
#
# [156] Binary Tree Upside Down
#
# https://leetcode.com/problems/binary-tree-upside-down/description/
#
# algorithms
# Medium (56.19%)
# Likes:    330
# Dislikes: 1024
# Total Accepted:    66.1K
# Total Submissions: 117.5K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the root of a binary tree, turn the tree upside down and return the new
# root.
# 
# You can turn a binary tree upside down with the following steps:
# 
# 
# The original left child becomes the new root.
# The original root becomes the new right child.
# The original right child becomes the new left child.
# 
# 
# 
# 
# The mentioned steps are done level by level, it is guaranteed that every node
# in the given tree has either 0 or 2 children.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,5]
# Output: [4,5,2,null,null,3,1]
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree will be in the range [0, 10].
# 1 <= Node.val <= 10
# Every node has either 0 or 2 children.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    145/145 cases passed (36 ms)
    Your runtime beats 45.14 % of python3 submissions
    Your memory usage beats 52.78 % of python3 submissions (14.3 MB)
    '''
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        return self.helper(root, None)
    
    def helper(self, node, parent):
        if not node:
            return parent
        
        newRoot = self.helper(node.left, node)
        node.left = parent.right if parent else None
        node.right = parent

        return newRoot


        
# @lc code=end

