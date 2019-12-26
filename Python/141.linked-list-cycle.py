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
    '''
    # Solution 1:  √ Your runtime beats 77.23 % of python submissions
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
    '''

    '''
    # Soluiton 2: Your runtime beats 98.65 % of python submissions
    def hasCycle(self, head):
        if not head or head.next==None:
            return False

        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
    '''

    # solution 3
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or head.next==None:
            return False

        slow,fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                return True
            
            slow = slow.next
            fast = fast.next.next
        return False

