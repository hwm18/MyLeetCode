#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (49.94%)
# Likes:    2640
# Dislikes: 93
# Total Accepted:    279.2K
# Total Submissions: 558.4K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given the head of a singly linked list where elements are sorted in ascending
# order, convert it to a height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# 
# Example 1:
# 
# 
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the
# shown height balanced BST.
# 
# 
# Example 2:
# 
# 
# Input: head = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [0]
# Output: [0]
# 
# 
# Example 4:
# 
# 
# Input: head = [1,3]
# Output: [3,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in head is in the range [0, 2 * 10^4].
# -10^5 <= Node.val <= 10^5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        p = head
        n = 0
        while p:            
            p = p.next
            n +=1
        
        # Recursively form a BST out of linked list from l --> r
        def helper(start, end):
            nonlocal head

            # Invalid case
            if start > end:
                return None
            
            mid = (start + end) //2  
            # First step of simulated inorder traversal. Recursively form
            # the left half      
            left = helper(start, mid-1)
            # Once left half is traversed, process the current node
            node = ListNode(head.val)
            node.left = left
            
            # Maintain the invariance mentioned in the algorithm
            head = head.next

            # Recurse on the right hand side and form BST out of them
            node.right = helper(mid+1, end)
            return node

        return helper(0, n-1)

    
        


        
# @lc code=end

