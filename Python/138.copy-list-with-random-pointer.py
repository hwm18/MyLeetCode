#
# @lc app=leetcode id=138 lang=python
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (26.96%)
# Likes:    1524
# Dislikes: 417
# Total Accepted:    244.2K
# Total Submissions: 905.1K
# Testcase Example:  '{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}'
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input:
# 
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
# 
# Explanation:
# Node 1's value is 1, both of its next and random pointer points to Node 2.
# Node 2's value is 2, its next pointer points to null and its random pointer
# points to itself.
# 
# 
# 
# 
# Note:
# 
# 
# You must return the copy of the given head as a reference to the cloned
# list.
# 
# 
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    '''
    # solution 1: Your runtime beats 36.97 % of python submissions
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        mp={}
        newhead = Node(head.val, None,None)
        mp[head] = newhead
        p = head
        q = newhead
        # copy node
        while p:
            q.random = p.random
            if p.next == None:                
               q.next = None
            else:
                q.next =  Node(p.next.val,None,None)
                mp[p.next] = q.next

            p = p.next
            q=q.next

        # copy random
        # for n in mp:
        #     curr = mp[n]
        #     if n.random:
        #         curr.random = mp[n.random]

        p = newhead
        while p:
            if p.random:
                p.random = mp[p.random]
            p = p.next

        return newhead
    '''

    '''
    soluiton 2: 
    19/19 cases passed (44 ms)
    Your runtime beats 57.36 % of python submissions
    Your memory usage beats 73.84 % of python submissions (14.3 MB)
    '''
    def copyRandomList(self, head):
        if not head:
            return None
        
        # copy node
        p = head
        while p:
            copy = Node(p.val, None,None)
            next = p.next            
            p.next = copy
            copy.next = next
            p = next

        # copy random
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

        # split
        newhead = head.next
        p,q=head,newhead
        while q.next:
            p.next = q.next
            p = p.next
            q.next = p.next
            q = q.next
        p.next = None
        q.next = None
        return newhead
        

