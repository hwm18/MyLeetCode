#
# @lc app=leetcode id=25 lang=python
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (38.20%)
# Likes:    1443
# Dislikes: 290
# Total Accepted:    211.3K
# Total Submissions: 553.1K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
#
#
#
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if self.get_length(head) < k:
            return head

        pre = None
        curr = head
        count = k
        while curr and count > 0:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
            count -= 1

        # pre is the new head
        # head is the new tail
        # curr is the next list
        head.next = self.reverseKGroup(curr, k)
        return pre

    def get_length(self, head):
        count = 0
        p = head
        while p:
            count += 1
            p = p.next
        return count


# @lc code=end

