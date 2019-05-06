#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/
#
# algorithms
# Easy (42.18%)
# Total Accepted:    1.5M
# Total Submissions: 3.6M
# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
# 
#
class Solution(object):
    #   √ Your runtime beats 77.23 % of python submissions
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or head.next==None:
            return False
        
        slow, fast=head,head
        while fast:
            if fast.next == None:
                return False           
            
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False



