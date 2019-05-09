#
# @lc app=leetcode id=270 lang=python
#
# [270] closest-binary-search-tree-value
#
# https://www.lintcode.com/problem/closest-binary-search-tree-value/description
#
# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
# 
# Example1
# Input: root = {5,4,9,2,#,8,10} and target = 6.124780
# Output: 5
# 
# Example 2:
# Input: root = {3,2,4,1} and target = 4.142857
# Output: 4
# 
#
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    def closestValue(self, root, target):
        if root is None:
            return None
            
        leftBound = self.findLeftBound(root,target)
        rightBound = self.findRightBound(root, target)
        if leftBound is None:
            return rightBound.val
        if rightBound is None:
            return leftBound.val
            
        if target-leftBound.val > rightBound.val -target:
            return rightBound.val
        
        return leftBound.val
    
    def findLeftBound(self, root,target):
        if root is None:
            return None
            
        if root.val >target:
            return self.findLeftBound(root.left,target)
        
        right = self.findLeftBound(root.right,target)
        
        return root if right is None else right
        
    def findRightBound(self, root,target):
        if not root:
            return None
            
        if root.val <=target:
           return self.findRightBound(root.right,target)
        
        left = self.findRightBound(root.left,target)
        if left is not None:
            return left
        return root
        
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    
    '''
    def closestValue(self, root, target):
        # write your code here
        if not root:
            return -1
        
        self.diff,self.ans = -1,0
        self.helper(root,0,target)
        return self.ans
    
    # O(n) Solution 
    def helper(self, root,level, target):
        if not root:
            return
        
        if self.diff==-1 or self.diff > abs(root.val-target):
            self.diff = abs(root.val-target)
            self.ans = root.val
        if(root.val > target):
            self.helper(root.left, level+1, target)
        else:
            self.helper(root.right, level+1, target)
    '''





