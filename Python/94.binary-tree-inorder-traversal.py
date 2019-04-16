#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (55.93%)
# Total Accepted:    438K
# Total Submissions: 783K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# Output: [1,3,2]
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # corner case
        if root is None:
            return []

        # 创建一个 dummy node，右指针指向 root
        # 并放到 stack 里，此时 stack 的栈顶 dummy
        # 是 iterator 的当前位置
        # iterative beats 81.92 %
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        result = []
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                result.append(stack[-1].val)

        # recursive version beats 16.82 %
        # self.inorder(root, result)

        return result

    # recursive version beats 16.82 %
    def inorder(self, root, result):
        if not root:
            return result

        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)

