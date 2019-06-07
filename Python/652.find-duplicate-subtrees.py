#
# @lc app=leetcode id=652 lang=python
#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (45.44%)
# Likes:    756
# Dislikes: 153
# Total Accepted:    37.5K
# Total Submissions: 82.4K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# Given a binary tree, return all duplicate subtrees. For each kind of
# duplicate subtrees, you only need to return the root node of any one of
# them.
# 
# Two trees are duplicate if they have the same structure with same node
# values.
# 
# Example 1: 
# 
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
# 
# 
# The following are two duplicate subtrees:
# 
# 
# ⁠     2
# ⁠    /
# ⁠   4
# 
# 
# and
# 
# 
# ⁠   4
# 
# Therefore, you need to return above trees' root in the form of a list.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Your runtime beats 75.47 % of python submissions
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.m,self.ans = {},[]
        print(self.inorder(root))

        return self.ans

    def inorder(self, node):
        if (not node):
            return ""

        Str = "("
        Str += self.inorder(node.left)
        Str += str(node.val)
        Str += self.inorder(node.right)
        Str += ")"

        # Subtree already present (Note that
        # we use unordered_map instead of
        # unordered_set because we want to print
        # multiple duplicates only once, consider
        # example of 4 in above subtree, it
        # should be printed only once.
        if (Str in self.m and self.m[Str] == 1):
            self.ans.append(node)
        
        self.m[Str] = self.m.get(Str, 0) +1
        # if Str in self.m:
        #     self.m[Str] += 1
        # else:
        #     self.m[Str] = 1

        return Str
        

