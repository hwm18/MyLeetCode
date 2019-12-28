#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 2: Your runtime beats 74.33 % of python3 submissions
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right and root.val == sum:
            return True
        
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    '''
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        self.result = False
        self.helper(root, 0,sum)
        return self.result
    
    # Solution 1: Your runtime beats 89.32 % of python3 submissions
    def helper(self, root, currSum, sum):
        if not root:
            return

        currSum += root.val
        if root.left==None and root.right==None:
            if currSum == sum:
                self.result = True
                return
            
        self.helper(root.left, currSum, sum)
        self.helper(root.right, currSum, sum)
    '''
    
        
# @lc code=end

