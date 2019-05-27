#
# @lc app=leetcode id=498 lang=python
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (45.33%)
# Likes:    349
# Dislikes: 225
# Total Accepted:    42.5K
# Total Submissions: 93.9K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of M x N elements (M rows, N columns), return all elements of
# the matrix in diagonal order as shown in the below image.
# 
# 
# 
# Example:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# Output:  [1,2,4,7,5,3,6,8,9]
# 
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# The total number of elements of the given matrix will not exceed 10,000.
# 
#
class Solution(object):
    # 根据题意顺序输出数组，注意边界判定即可。
    # Your runtime beats 64.97 % of python submissions
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix)==0 or len(matrix[0])==0:
            return []
        m,n = len(matrix),len(matrix[0])
        ans, flag = [], True
        i,j=0,0
        while( i < m and j<n):
            # left, buttom -> right, top
            if flag:
                while(i>0 and j<n-1):
                    ans.append(matrix[i][j])
                    i -=1
                    j +=1
                ans.append(matrix[i][j])
                if j != n-1:
                    j += 1
                else:
                    i += 1
            else: # right, top -> left, buttom
                while(i<m-1 and j>0):
                    ans.append(matrix[i][j])
                    i +=1
                    j -=1
                ans.append(matrix[i][j])
                if i != m-1:
                    i += 1
                else:
                    j += 1

            flag = not flag

        return ans
    '''
    # 根据题意顺序输出数组，注意边界判定即可。
    # Your runtime beats 43.53 % of python submissions
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix)==0 or len(matrix[0])==0:
            return []
        n,m = len(matrix),len(matrix[0])
        ans = []
        i,j=0,0
        dd = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                dd[i+j+1].append(matrix[i][j])
        
        for i,v in dd.iteritems():
            if i%2==1:
                dd[i].reverse()
            ans += dd[i]
        return ans
    '''



