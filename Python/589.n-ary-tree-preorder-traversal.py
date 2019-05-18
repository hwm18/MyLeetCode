#
# @lc app=leetcode id=589 lang=python
#
# [589] N-ary Tree Preorder Traversal
#
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/
#
# algorithms
# Easy (67.22%)
# Likes:    214
# Dislikes: 33
# Total Accepted:    40.5K
# Total Submissions: 60.2K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Given an n-ary tree, return the preorder traversal of its nodes' values.
# 
# For example, given a 3-ary tree:
# 
# 
# 
# 
# 
# 
# 
# Return its preorder traversal as: [1,3,5,6,2,4].
# 
# 
# 
# Note:
# 
# Recursive solution is trivial, could you do it iteratively?
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
    # solution 2: Your runtime beats 52.96 % of python submissions
    def preorder(self, root):
		if not root:
			return []       # return empty list in case of empty Node object

		result = [root.val]     # add first node
		for child in root.children:     # iterate through all children
			result.extend(self.preorder(child))     # repeat the process but root is now child
													# this way you can go through the whole tree
		return result
    
    '''    
    # soltuion 1:  Your runtime beats 48.3 % of python submissions
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        self.ans = []
        self.helper(root)
        return self.ans
    
    def helper(self, root):
        if not root:
            return
        
        self.ans.append(root.val)
        #self.helper(root.children)
        for node in root.children:
            self.helper(node)
    '''
        

