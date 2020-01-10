#
# @lc app=leetcode id=891 lang=python3
#
# [891] Sum of Subsequence Widths
#

# @lc code=start
class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:        
        '''
        # Solution 1: brute force  O(n**2)
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                sum += (A[j]-A[i]) * 2*(j-i-1)
        '''
        if not A or len(A)==0:
            return 0

        # solution: O(n) - Your runtime beats 40.78 % of python3 submissions
        # for A[i]:
        #  sum -= A[i] * pow2(n-1-i)
        #  sum += A[i] * pow(i)
        M = 10**9 +7
        
        pow2 = [1] * 20000        
        for i in range(1, 20000):
            pow2[i] = pow2[i-1] *2 %M
        
        n = len(A)
        sum = 0
        #list.sort(A)
        A.sort()
        '''
        for i in range(n):
            sum += A[i] * pow2[i] %M
            sum -= A[i] * pow2[n-1-i] %M
            sum %= M
        '''
        # improve - Your runtime beats 53.4 % of python3 submissions
        for i, val in enumerate(A):
            sum = (sum + (pow2[i] - pow2[n-1-i]) * val) % M

        return sum

# @lc code=end

