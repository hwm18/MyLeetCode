#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    创建head.
    找到m的前一个节点-Pre
    记录Pre的下一个节点，它会是翻转链的尾部。
    翻转指定区间的链表，翻到最后一个节点时，把reverseTail.next指向它的next。这样就把翻转链表与之后
    的链表接起来了。
    返回dummynode的下一个节点。
    '''
    # Your runtime beats 85.79 % of python3 submissions
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m>= n or not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        node = dummy

        for i in range(1,m):
            if not node:
                return None
            node = node.next
        
        premNode, mNode = node, node.next
        nNode, postNnode = mNode, mNode.next
        i = m
        while(i<n):
            if postNnode == None:
                return None
            next = postNnode.next
            postNnode.next = nNode
            nNode = postNnode
            postNnode = next
            i+=1
        
        premNode.next = nNode
        mNode.next = postNnode
        return dummy.next
        

