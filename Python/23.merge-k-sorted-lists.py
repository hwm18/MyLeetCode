#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappush, heappop, heapreplace, heapify
class Solution:
    # solution 1: heapq
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists)==0:
            return None
       
        dummy = ListNode(0)
        node = dummy
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while  h:
            v, n = h[0]
            if n.next is None:
                heappop(h) # only change heap size when necessary
            else:
                heapreplace(h, (n.next.val,n.next))
            node.next = n
            node = node.next 
        
        return dummy.next

    '''   
    # Solution 2: divide-conque: Your runtime beats 76.09 % of python3 submissions
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists)==0:
            return None
        
        return self.helper(lists,0,len(lists)-1)
   

    def helper(self, lists, start, end):
        if start>= end:
            return lists[start]
        mid = start  + (end - start)//2
        left = self.helper(lists,start, mid)
        right = self.helper(lists,mid+1, end)
        return self.merge(left,right)
    
    def merge(self, left, right):
        dummy = ListNode(0)
        head = dummy
        while left and right:
            if left.val <right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next 
            head = head.next
        
        if left:
            head.next = left
        else:
            head.next = right
        return dummy.next
     '''

# @lc code=end

