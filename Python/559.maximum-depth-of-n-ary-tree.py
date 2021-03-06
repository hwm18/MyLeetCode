#
# @lc app=leetcode id=559 lang=python
#
# [559] Maximum Depth of N-ary Tree
#
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
#
# algorithms
# Easy (65.50%)
# Likes:    337
# Dislikes: 19
# Total Accepted:    45.2K
# Total Submissions: 69.1K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Given a n-ary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# For example, given a 3-ary tree:
# 
# 
# 
# 
# 
# 
# We should return its max depth, which is 3.
# 
# 
# 
# Note:
# 
# 
# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.
# 
# 
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution(object):
    '''
    # Solution 1: Your runtime beats 55.04 % of python submissions
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        
        ans = 0
        for child in root.children:
            ans = max(ans, self.maxDepth(child))
        return ans +1
    '''

    # Solution 2: Your runtime beats 52.87 % of python submissions
    def maxDepth(self, root):
        if not root: return 0
        if not root.children: return 1
        height = [self.maxDepth(node) for node in root.children]
        return max(height) + 1

