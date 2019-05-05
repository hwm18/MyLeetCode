#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    # Your runtime beats 79.58 % of python3 submissions
    def reverseKGroup(self, head, k):
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k: return head
        new_head, prev = self.reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return prev
    
    def reverse(self, head, count):
        prev, cur, nxt = None, head, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev)
    '''
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr, cnt = head, 0
        while curr and cnt<k:
            curr = curr.next
            cnt+=1

        if cnt<k:
            return head
        new_head, pre = self.reverse(head, cnt)
        head.next = self.reverseKGroup(new_head,k)
        
        return pre
    
    def reverse(self, head, cnt):
        pre, curr = None, head
        while cnt>0:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
            cnt -=1
        return (curr, pre)

