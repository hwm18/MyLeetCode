#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # in-order traver
    '''
    77/77 cases passed (40 ms)
    Your runtime beats 90.47 % of python3 submissions
    Your memory usage beats 23.92 % of python3 submissions (17 MB)
    '''
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        self.pre = None
        return self.helper(root)
    
    def helper(self, root):
        if not root:
            return True
        
        if(self.helper(root.left)):
            if self.pre and self.pre.val >= root.val:
                return False
            self.pre = root
            return self.helper(root.right)

        return False



    '''
    77/77 cases passed (36 ms)
    Your runtime beats 97.37 % of python3 submissions
    Your memory usage beats 56.35 % of python3 submissions (16.5 MB)
    '''
    '''
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return self.helper(root, None, None)


    def helper(self, root, low, high):
        if not root:
            return True
        
        return (low==None or root.val>low) and (high==None or root.val<high) and self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)
    '''

    '''
    # solution 5: Your runtime beats 81.74 % of python3 submissions
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        min_val,max_val = -math.inf,math.inf
        return self.helperBST(root, min_val,max_val)
    
    def helperBST(self, root, min_value, max_value):
        if not root:
            return True

        if root.val<=min_value or root.val>=max_value:
            return False
        
        left = self.helperBST(root.left, min_value, root.val)
        right = self.helperBST(root.right, root.val, max_value)
        if not left or not right:
            return False
        
        return True

    # # Method 3: Your runtime beats 53.25 % of python3 submissions
    # def isValidBST(self, root: TreeNode) -> bool:
    #     if not root:
    #         return True
    #     isBST, minNode, maxNode = self.divideConquer(root)
    #     return isBST
    
    def divideConquer(self, root):
        if root is None:
            return True, None, None

        left_isBST, left_minNode, left_maxNode = self.divideConquer(root.left)
        right_isBST, right_minNode, right_maxNode = self.divideConquer(root.right)
        if not left_isBST or not right_isBST:
            return False, None,None
        
        if left_maxNode is not None and left_maxNode.val >= root.val:
            return False, None, None
        if right_minNode is not None and right_minNode.val <= root.val:
            return False, None, None
        
        minNode = left_minNode if left_minNode is not None else root
        maxNode = right_maxNode if right_maxNode is not None else root
        return True, minNode, maxNode
    '''

    '''
    # Method2:  Your runtime beats 18.98 % of python3 submissions
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        stack = []
        while root:
            stack.append(root)
            root = root.left

        last = stack[-1]
        while stack:
            curr = stack[-1]

            if curr.right==None:
                curr = stack.pop()
                while(stack and stack[-1].right == curr):
                    curr = stack.pop()
            else:
                curr = curr.right
                while curr:
                    stack.append(curr)
                    curr = curr.left
            if stack:
                if stack[-1].val <= last.val:
                    return False
                last = stack[-1]

        return True
    '''

    '''
    # Method 1: Your runtime beats 53.12 % of python3 submissions
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.last, self.result = None, True
        self.helper(root)
        return self.result
    
    def helper(self, root):
        if not root:
            return
        
        left=self.helper(root.left)
        if self.last !=None and self.last.val >= root.val:
            self.result = False
            return
        self.last = root

        right = self.helper(root.right)
    '''

    '''
    # Method 4: check the result array of inorder 
    def isValidBST(self, root):
        output = []
        self.inOrder(root, output)
        
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False

        return True

    def inOrder(self, root, output):
        if root is None:
            return
        
        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)
    '''


