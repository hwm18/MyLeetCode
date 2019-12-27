#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
class Solution:
    # Solution 1: merge sort - Your runtime beats 46.09 % of python3 submissions
    # Soluton 2: quick sort - Your runtime beats 72.78 % of python3 submissions
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums or len(nums)==0:
            return []
        
        #return self.merge_sort(nums)
        #return self.quick_sort(nums)
        #return self.bubble_sort(nums)
        #return self.insert_sort(nums)
        #return self.selection_sort(nums)
        return self.heapSort(nums)
    
    # Solution 6: @heapSort - Your runtime beats 6.04 % of python3 submissions
    def heapSort(self, nums):
        def heapify(nums, n, i): 
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            
            if l < n and nums[i] < nums[l]: 
                largest = l 

            if r < n and nums[largest] < nums[r]: 
                largest = r 

            if largest != i: 
                nums[i], nums[largest] = nums[largest], nums[i]
                
                heapify(nums, n, largest)
                
        n = len(nums) 

        for i in range(n, -1, -1): 
            heapify(nums, n, i) 

        for i in range(n-1, 0, -1): 
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0) 
        return nums
    
    # Soltuion 5: @selectionSort, TLE Time Limit Exceeded - 9/10 cases passed (N/A)
    def selection_sort(self, nums):
        for i in range(len(nums)):
            _min = min(nums[i:])
            min_index = nums[i:].index(_min)
            nums[i + min_index] = nums[i]
            nums[i] = _min
        return nums

    # Solution 4: insert sort - Time Limit Exceeded - 8/10 cases passed (N/A)
    def insert_sort(self, nums):
        if not nums or len(nums)==0:
            return []
        
        for i in range(1, len(nums)):
            key = nums[i]
            j = i-1
            while j>=0 and key<nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            
            nums[j+1] = key

        return nums

    
    # Solution 3: bubble sort - Time Limit Exceeded - 8/10 cases passed (N/A)
    def bubble_sort(self,nums):
        if not nums or len(nums)==0:
            return []

        n = len(nums)
        for i in range(n):
            for j in range(0,n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        return nums

    
    # solution 2: Your runtime beats 72.78 % of python3 submissions
    def quick_sort(self, nums):
        def helper(start, end):
            if start >=end:
                return
            l,r = start,end
            mid = l + (r - l) //2
            p = nums[mid]
            while l <= r:
                while  l<= r and nums[l] < p:
                    l += 1
                while  l<= r and nums[r] > p:
                    r -= 1
                
                if l <=r:
                    nums[l],nums[r] = nums[r],nums[l]
                    l += 1
                    r -= 1

            helper(start, r)
            helper(l,end)

        helper(0, len(nums)-1)
        return nums

    # Solution 1: merge sort - Your runtime beats 46.09 % of python3 submissions
    def merge_sort(self, nums):
        if len(nums)<=1:
            return nums

        mid = len(nums)//2
        left = self.merge_sort(nums[0:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        
        results = []
        m,n=len(left),len(right)
        i,j=0,0
        while i<m and j<n:
            if left[i]<right[j]:
                results.append(left[i])
                i += 1
            else:
                results.append(right[j])
                j += 1
        
        results.extend(left[i:])
        results.extend(right[j:])
        # while i<m:
        #     results.append(left[i])
        #     i += 1
        # while j < n:
        #     results.append(right[j])
        #     j += 1

        return results

        
# @lc code=end

