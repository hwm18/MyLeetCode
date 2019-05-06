#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        fast = middle = head
        reverse = None

        # find the middle node and reverse node before middle
        while fast and fast.next:
            fast = fast.next.next
            current, middle = middle, middle.next
            current.next, reverse = reverse, current

        if fast:  # mean list has odd count nodes, need change to next.
            middle = middle.next

        # check the reverse equal the middle
        while reverse:
            if reverse.val != middle.val:
                return False
            reverse = reverse.next
            middle = middle.next

        return True

