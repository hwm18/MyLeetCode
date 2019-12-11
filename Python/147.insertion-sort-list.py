#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        while head:
            node = dummy
            while node.next and node.next.val <= head.val:
                node = node.next
            
            next = head.next 
            head.next = node.next 
            node.next = head 
            head = next
        return dummy.next



        
# @lc code=end

