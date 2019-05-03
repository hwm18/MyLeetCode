#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        if not root:
            return
        
        list_val, list_node = [],[]
        self.inorder(root, list_val, list_node)
        
        list_val.sort()
        for i in range(len(list_val)):
            list_node[i].val = list_val[i]
        
    def inorder(self, root, list_val, list_node):
        if not root:
            return
        
        self.inorder(root.left, list_val, list_node)
        list_val.append(root.val)
        list_node.append(root)
        self.inorder(root.right, list_val, list_node)


    '''
    def recoverTree(self, root: TreeNode) -> None:
        if not root:
            return

        self.node1, self.node2 = None, None
        self.lastElement = None

        self.helper(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val
    
    def helper(self, root):
        if not root:
            return
        
        self.helper(root.left)

        if(self.node1 == None and self.lastElement != None 
            and self.lastElement.val > root.val):
            self.node1 = self.lastElement

        if(self.node1 != None and self.lastElement != None 
            and self.lastElement.val > root.val):
            self.node2 = root
            
        self.lastElement = root
        
        self.helper(root.right)
        '''

       
            

