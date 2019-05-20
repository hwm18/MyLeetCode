#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (31.08%)
# Likes:    5132
# Dislikes: 1304
# Total Accepted:    866.3K
# Total Submissions: 2.8M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    # soluiton 2: Your runtime beats 96.7 % of python submissions
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = ListNode(-1)
        head = dummy
        r,s = 0,0
        while l1 or l2 or r:
            v1 =v2 =0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 =l2.next

            s = r + v1 + v2
            r = s //10
            head.next = ListNode(s%10)            
            head = head.next
        
        return dummy.next

    # Solution 1: Your runtime beats 99.34 % of python submissions
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = ListNode(-1)
        head = dummy
        r,s = 0,0
        while l1 and l2:
            s = r + l1.val + l2.val
            r = s //10
            head.next = ListNode(s%10)
            l1 = l1.next
            l2 = l2.next
            head = head.next
        while l1:
            s = r + l1.val
            r = s //10
            head.next = ListNode(s%10)
            l1 = l1.next
            head =head.next
        
        while l2:
            s = r + l2.val
            r = s //10
            head.next = ListNode(s%10)
            l2 = l2.next
            head =head.next
        if r>0:
           head.next = ListNode(r)
           head = head.next
        return dummy.next
        

