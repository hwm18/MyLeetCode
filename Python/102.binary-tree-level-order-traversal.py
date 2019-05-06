#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    # method 2: use deque -  Your runtime beats 21.02 % of python3 submissions
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue, result = deque([root]),[]
        while queue:
            size, level = len(queue),[]
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
    '''
    # method 1: two queues - Your runtime beats 78.62 % of python3 submissions
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue, result = [root],[]
        while queue:
            new_queue=[]
            result.append([node.val for node in queue])
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
            
        return result
    '''

