#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/
#
# algorithms
# Medium (42.01%)
# Likes:    321
# Dislikes: 52
# Total Accepted:    21.5K
# Total Submissions: 51.2K
# Testcase Example:  '{"$id":"1","child":null,"next":{"$id":"2","child":null,"next":{"$id":"3","child":{"$id":"7","child":null,"next":{"$id":"8","child":{"$id":"11","child":null,"next":{"$id":"12","child":null,"next":null,"prev":{"$ref":"11"},"val":12},"prev":null,"val":11},"next":{"$id":"9","child":null,"next":{"$id":"10","child":null,"next":null,"prev":{"$ref":"9"},"val":10},"prev":{"$ref":"8"},"val":9},"prev":{"$ref":"7"},"val":8},"prev":null,"val":7},"next":{"$id":"4","child":null,"next":{"$id":"5","child":null,"next":{"$id":"6","child":null,"next":null,"prev":{"$ref":"5"},"val":6},"prev":{"$ref":"4"},"val":5},"prev":{"$ref":"3"},"val":4},"prev":{"$ref":"2"},"val":3},"prev":{"$ref":"1"},"val":2},"prev":null,"val":1}'
#
# You are given a doubly linked list which in addition to the next and previous
# pointers, it could have a child pointer, which may or may not point to a
# separate doubly linked list. These child lists may have one or more children
# of their own, and so on, to produce a multilevel data structure, as shown in
# the example below.
# 
# Flatten the list so that all the nodes appear in a single-level, doubly
# linked list. You are given the head of the first level of the list.
# 
# 
# 
# Example:
# 
# 
# Input:
# ⁠1---2---3---4---5---6--NULL
# ⁠        |
# ⁠        7---8---9---10--NULL
# ⁠            |
# ⁠            11--12--NULL
# 
# Output:
# 1-2-3-7-8-11-12-9-10-4-5-6-NULL
# 
# 
# 
# 
# Explanation for the above example:
# 
# Given the following multilevel doubly linked list:
# 
# 
# 
# 
# 
# 
# We should return the following flattened doubly linked list:
# 
# 
# 
# 
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    '''
    # solution 1: Your runtime beats 24.44 % of python3 submissions
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return None
        def travel(node):
            while node:
                q = node.next
                if not q: tail = node
                if node.child:
                    node.next = node.child
                    node.child.prev = node
                    t = travel(node.child)
                    if q:
                        q.prev = t
                    t.next= q
                    node.child = None
                node = node.next
            return tail

        travel(head)
        return head
    '''

    #  Your runtime beats 84.85 % of python3 submissions
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        stack = [head]
        pre = None
        while stack:
            q = stack.pop()
            if pre:
                q.prev = pre
                pre.next = q
                
            pre = q
            if q.next:
                stack.append(q.next)
            if q.child:
                stack.append(q.child)
                q.child = None
        return head


