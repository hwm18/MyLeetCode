#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii/
#
# algorithms
# Easy (42.18%)
# Total Accepted:    1.5M
# Total Submissions: 3.6M
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Note: Do not modify the linked list.

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
#
class Solution(object):
    # Your runtime beats 52.89 % of python submissions
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                while head != fast:
                    head = head.next
                    fast = fast.next
                return head
        return None
        
    
    ''' Method 2: # Your runtime beats 26.24 % of python submissions
        self.slow, self.fast = None, None
        if not (self.hasCycle(head)):
            return None

        self.slow = head
        while self.fast!=self.slow:
            self.fast = self.fast.next
            self.slow = self.slow.next
        return self.slow

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        
        self.slow, self.fast=head,head
        while self.fast:
            if self.fast.next == None:
                return False           
            
            self.fast = self.fast.next.next
            self.slow = self.slow.next
            if self.slow == self.fast:
                return True
        return False
    '''




