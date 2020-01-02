#
# @lc app=leetcode id=845 lang=python3
#
# [845] Longest Mountain in Array
#

# @lc code=start
class Solution:
    # find mountain O(logN); find longest mountain O(N)
    def longestMountain(self, A: List[int]) -> int:
        if not A or len(A)==0:
            return 0
        
        start, result = None, 0
        i, n = 0,len(A)
        while i<n-1:
            if A[i] < A[i+1]:
                start = i
                while  i+1 < n and A[i]<A[i+1]:
                    i += 1
            elif A[i]==A[i+1]:
                i += 1
                start = None
            else:
                i+=1
                if start != None:
                    result = max(result, i-start +1)
        
        return result
                 


        
# @lc code=end

