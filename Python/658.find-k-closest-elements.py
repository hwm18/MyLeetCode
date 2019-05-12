#
# @lc app=leetcode id=658 lang=python
#
# [658] Find K Closest Elements
#
class Solution(object):
    # Your runtime beats 56.47 % of python submissions
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if not arr:
            return []
        n = len(arr)        
        if(k>n):
            return arr
        
        # lo, hi = 0, n-k
        # while lo<hi:
        #     mid = (lo + hi)//2
        #     if x-arr[mid]>arr[mid+k]-x:
        #         lo = mid + 1
        #     else:
        #         hi = mid
        # return arr[lo:lo+k]
        start, end = 0, n - k
        while start < end:
            mid =start + (end - start) // 2
            if  abs(x-arr[mid]) > abs(arr[mid+k] - x):
                start = mid +1
            else:
                end = mid
        
        return arr[start:start+k]

    '''
    #   Your runtime beats 43.01 % of python submissions
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        index = self.firstIndex(arr, x)
        left, right = index - 1, index
        result = []
        for i in range(k):
            if left < 0:
                result.append(arr[right])
                right += 1
            elif right == n:
                result.append(arr[left])
                left -= 1
            else:
                if x - arr[left] <= arr[right] - x: 
                    result.append(arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1
                    
        return sorted(result)
        
    def firstIndex(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        
        if A[start] >= target:
            return start
            
        if A[end] >= target:
            return end
            
        return len(A)
    '''
        
        

        

