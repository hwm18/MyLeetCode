#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        mid = self.findmid(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        return self.merge(left,right)
    
    def findmid(self, head):
        slow,fast = head,head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
        return slow
    
    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        
        dummy = ListNode(0)
        head = dummy
        while left and right:
            if left.val<right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next
        
        if left:
            head.next = left
        elif right:
            head.next = right

        return dummy.next

        
# @lc code=end

