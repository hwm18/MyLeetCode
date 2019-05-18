#
# @lc app=leetcode id=429 lang=python
#
# [429] N-ary Tree Level Order Traversal
#
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Easy (59.22%)
# Likes:    230
# Dislikes: 29
# Total Accepted:    31.2K
# Total Submissions: 52.8K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Given an n-ary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# For example, given a 3-ary tree:
# 
# 
# 
# 
# 
# 
# 
# We should return its level order traversal:
# 
# 
# [
# ⁠    [1],
# ⁠    [3,2,4],
# ⁠    [5,6]
# ]
# 
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
from collections import deque
class Solution(object):
    '''
    # solution 1: Your runtime beats 48.35 % of python submissions
    def levelOrder(self, root) :
        ans=[]
        def traveser(root, level):
            if not root:
                return

            if level==len(ans):
                ans.append([])
            ans[level].append(root.val)
            if root.children:
                for child in root.children:
                    traveser(child,level+1)

        traveser(root,0)
        return ans

    '''
    # solution 2: Your runtime beats 51.24 % of python submissions
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        ans=[]
        q = deque()
        q.append(root)
        while q:
            level=[]
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                for child in node.children:
                    q.append(child)
            ans.append(level)
        return ans
        
        '''
        queue = [root] if root else []
        ans = [] 
        
        while queue:
            ans.append([node.val for node in queue])
            queue = [child for node in queue for child in node.children]    
            
        return ans
        '''

