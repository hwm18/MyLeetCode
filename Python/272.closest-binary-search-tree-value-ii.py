#
# @lc app=leetcode id=272 lang=python
#
# [272] closest-binary-search-tree-value-ii
#
# https://www.lintcode.com/problem/closest-binary-search-tree-value-ii/description
#
# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
#
# Example 1:
# Input:
# {1}
# 0.000000
# 1
# Output:
# [1]

# Example 2:
# Input:
# {1,#,2,#,3,#,4}
# 0.275000
# 2
# Output:
# [1,2]
#
#
#
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """

    def closestKValues(self, root, target, k):
        # O(n) two steps: 1. inorder get a sorted array
        # 2. search the index >= target in the sorted array

        self.arr = []
        self.traverse(root)

        # Binary search to find the closest item index in self.arr
        n = len(self.arr)
        if n == k:
            return self.arr
        i = 0
        while i < n:
            if self.arr[i] >= target:
                break
            i += 1
        if i >= n:
            return self.arr[n - k : n]

        ans = []
        left, right = i - 1, i
        for t in range(k):
            if left >= 0 and (
                right >= n or target - self.arr[left] < self.arr[right] - target
            ):
                ans.append(self.arr[left])
                left -= 1
            else:
                ans.append(self.arr[right])
                right += 1
        return ans

    def traverse(self, root):
        if not root:
            return

        self.traverse(root.left)
        self.arr.append(root.val)
        self.traverse(root.right)

