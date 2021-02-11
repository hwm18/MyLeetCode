#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (35.33%)
# Likes:    5099
# Dislikes: 370
# Total Accepted:    466.4K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3]'
#
# A path in a binary tree is a sequence of nodes where each pair of adjacent
# nodes in the sequence has an edge connecting them. A node can only appear in
# the sequence at most once. Note that the path does not need to pass through
# the root.
# 
# The path sum of a path is the sum of the node's values in the path.
# 
# Given the root of a binary tree, return the maximum path sum of any path.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 =
# 6.
# 
# 
# Example 2:
# 
# 
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7
# = 42.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 3 * 10^4].
# -1000 <= Node.val <= 1000
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
    94/94 cases passed (84 ms)
    Your runtime beats 81.5 % of python3 submissions
    Your memory usage beats 58.48 % of python3 submissions (21.7 MB)
    '''
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.result = float('-inf')
        def maxValue(node):
            if not node:
                return 0
            
            left = maxValue(node.left)
            right = maxValue(node.right)
            self.result = max(self.result, node.val + left+right)
            ret = node.val + max(left,right)
            return ret if ret>0 else 0
        
        maxValue(root)
        return self.result

    # solution 2:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0

            # max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # the price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain
            
            # update max_sum if it's better to start a new path
            max_sum = max(max_sum, price_newpath)
        
            # for recursion :
            # return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)
   
        max_sum = float('-inf')
        max_gain(root)
        return max_sum
        
# @lc code=end

