#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # method 2: Your runtime beats 93.37 % of python3 submissions
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head

        pre = None
        while head != None:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre


        '''
        # method 1
        return self.reverse(head, None)

    # Method 1: Your runtime beats 68.66 % of python3 submissions
    def reverse(self, head, pre):
        if head is None:
            return pre

        next = head.next
        head.next = pre
        
        return self.reverse(next, head)
    '''
        

