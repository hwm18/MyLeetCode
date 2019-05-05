#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Your runtime beats 92.71 % of python3 submissions
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy, dummy
        for i in range(n+1):
            fast = fast.next
        
        while fast != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next

    '''
    # method 2: two pass
    # Your runtime beats 92.71 % of python3 submissions
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        
        cnt=1
        curr = head
        while curr != None:
            cnt +=1
            curr = curr.next
        n %=cnt

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        i = 1
        while(i<cnt-n):
            curr = curr.next
            i+=1

        curr.next = curr.next.next
        return dummy.next
    '''

