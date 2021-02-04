#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (39.34%)
# Likes:    2110
# Dislikes: 791
# Total Accepted:    516.9K
# Total Submissions: 1.3M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^5].
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
    # BFS
    '''
    52/52 cases passed (896 ms)
    Your runtime beats 5.13 % of python3 submissions
    Your memory usage beats 71.75 % of python3 submissions (49.2 MB)
    '''
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
            
        queue = deque([root])
        depth = 1
        rightMost = root
        while queue:
            node = queue.popleft()
            # leaf
            if not node.left and not node.right:
                break
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
            
            if node == rightMost:
                depth +=1
                rightMost = node.right if node.right else node.left
        
        return depth

    '''
    52/52 cases passed (708 ms)
    Your runtime beats 10.33 % of python3 submissions
    Your memory usage beats 17.05 % of python3 submissions (53.1 MB)
    '''
    '''
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        if root.left == None:
            return self.minDepth(root.right) +1
        
        if root.right == None:
            return self.minDepth(root.left) +1 
        
        return min(self.minDepth(root.left), self.minDepth(root.right)) +1
    '''
# @lc code=end