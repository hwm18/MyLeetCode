#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#

# @lc code=start
import heapq
from heapq import * 
class Solution:
    @staticmethod
    def calculate_median(max_heap: List[int], min_heap: List[int]) -> float:
        if len(max_heap) == len(min_heap):
            return (-max_heap[0] + min_heap[0]) / 2.0
        return min_heap[0]
    
    @staticmethod
    def add_to_heaps(max_heap: List[int], min_heap: List[int], num) -> None:
        heappush(max_heap, -heappushpop(min_heap, num))
        
        if len(max_heap) > len(min_heap):
            heappush(min_heap, -heappop(max_heap))
    
    @staticmethod
    def remove_from_heap(heap: List[int], num) -> None:
        index = heap.index(num)
        # delete in O(1)
        # replace the value we want to remove with the last value
        heap[index] = heap[-1]
        del heap[-1]
        
        # Restore heap property thoughout the tree
        if index < len(heap):
            heapq._siftup(heap, index)
            heapq._siftdown(heap, 0, index)
            
    def remove_from_heaps(self, max_heap: List[int], min_heap: List[int], num) -> None:
        if min_heap[0] <= num:
            self.remove_from_heap(min_heap, num)
            return
        self.remove_from_heap(max_heap, -num)

    '''
    # Solution 1: Your runtime beats 41.57 % of python3 submissions
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap: List[int] = []
        min_heap: List[int] = []
        result: List[int] = []
        size_of_k = k - 1

        for i in range(size_of_k):
            self.add_to_heaps(max_heap, min_heap, nums[i])
        
        for i in range(size_of_k, len(nums)):
            self.add_to_heaps(max_heap, min_heap, nums[i])
            median = self.calculate_median(max_heap, min_heap)
            result.append(median)
            self.remove_from_heaps(max_heap, min_heap, nums[i - size_of_k ])
        
        return result
    '''

    # Solution 2: Your runtime beats 11.43 % of python3 submissions
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums or len(nums)==0 or k<1:
            return []
        
        results = []
        min_heap,max_heap=[],[]
        median = 0
        if k>1:
            heapq.heappush(max_heap, -nums[0])
            for i in range(1,k-1):
                curr = -1 * max_heap[0]
                if nums[i]<= curr:
                    heapq.heappush(max_heap, -nums[i])
                else:
                    heapq.heappush(min_heap, nums[i])
            median = -max_heap[0]
        
        k_is_even = (k & 1) == 0
        for i in range(k-1, len(nums)):
            # insert
            if nums[i]<= median:
                heapq.heappush(max_heap, -nums[i])
            else:
                heapq.heappush(min_heap, nums[i])
            # balance: maintain size
            while len(max_heap) > len(min_heap)+1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            while len(max_heap) < len(min_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

            # append result
            median = -max_heap[0]
            if k_is_even:
                median = (-max_heap[0] + min_heap[0]) * 0.5

            results.append(median)
            # remove from min_heap or max_heap
            if nums[i-k+1]<=median:
                max_heap.remove(-nums[i-k+1])
                heapq.heapify(max_heap)
            else:
                min_heap.remove(nums[i-k+1])
                heapq.heapify(min_heap)
        
        return results


# @lc code=end

