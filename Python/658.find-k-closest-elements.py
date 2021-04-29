#
# @lc app=leetcode id=658 lang=python
#
# [658] Find K Closest Elements
#
class Solution(object):
    # solution 4: 采用的是二分法 + 双指针 
    # 二分法确定一个位置，左侧是 < target，右侧是 >= target 
    # 然后用两根指针从中间向两边走，依次找到最接近的 k 个数
    def findClosestElements(self, arr, k, target):
        # 找到 A[left] < target, A[right] >= target
        # 也就是最接近 target 的两个数，他们肯定是相邻的
        right = self.findUpperClosest(arr, target)
        left = right - 1
    
    	# 两根指针从中间往两边扩展，依次找到最接近的 k 个数
        results = []
        for _ in range(k):
            if self.isLeftCloser(arr, target, left, right):
                results.append(arr[left])
                left -= 1
            else:
                results.append(arr[right])
                right += 1
        
        return sorted(results)  # return the sorted result
    
    def findUpperClosest(self, A, target):
        # find the first number >= target in A
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        
        if A[start] >= target:
            return start
        
        if A[end] >= target:            
            return end
        
        # 找不到的情况
        return len(A)
        
    def isLeftCloser(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target

    '''
    # solution 3:  Your runtime beats 36.92 % of python submissions
    def findClosestElements(self, arr, k, x):
        arr = sorted(arr, key = lambda y: abs(x-y))
        return sorted(arr[:k])
    '''

    '''
    # Solution 2: Your runtime beats 56.47 % of python submissions
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

    '''
    # solution 1:  Your runtime beats 43.01 % of python submissions
     # Algorithm:
        # 1. Find the first index that A[index] >= target
        # 2. Set two pointers left = index - 1 and right = index
        # 3. Compare A[left] and A[right] to decide which pointer should move
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
        
        

        

