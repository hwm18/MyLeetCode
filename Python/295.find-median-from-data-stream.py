#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
'''
The invariant of the algorithm is two heaps, small and large, each represent half of the current list. The length of smaller half is kept to be n / 2 at all time and the length of the larger half is either n / 2 or n / 2 + 1 depend on n’s parity.

This way we only need to peek the two heaps’ top number to calculate median.

Any time before we add a new number, there are two scenarios, (total n numbers, k = n / 2):


(1) length of (small, large) == (k, k)
(2) length of (small, large) == (k, k + 1)

After adding the number, total (n + 1) numbers, they will become:


(1) length of (small, large) == (k, k + 1)
(2) length of (small, large) == (k + 1, k + 1)

Here we take the first scenario for example, we know the large will gain one more item and small will remain the same size, but we cannot just push the item into large. What we should do is we push the new number into small and pop the maximum item from small then push it into large (all the pop and push here are heappop and heappush). By doing this kind of operations for the two scenarios we can keep our invariant.

Therefore to add a number, we have 3 O(log n) heap operations. Luckily the heapq provided us a function “heappushpop” which saves some time by combine two into one. The document says:

<blockquote>Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().</blockquote>

Alltogether, the add operation is O(logn), The findMedian operation is O(1).

Note that the heapq in python is a min heap, thus we need to invert the values in the smaller half to mimic a “max heap”.

A further observation is that the two scenarios take turns when adding numbers, thus it is possible to combine the two into one. For this please see stefan’s post
'''
# Solution: use two heap: max heap and min heap, keep the heap size len(min_heap) = len(max_heap) +1
# Your runtime beats 72.23 % of python3 submissions
from heapq import *
class MedianFinder:
    '''
    # solution 1: len(min_heap) = len(max_heap) +1
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = [] 
        self.min_heap = []
        
    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):# add num to self.min_heap
            heapq.heappush(self.min_heap, -heappushpop(self.max_heap, -num))
        else:
            heapq.heappush(self.max_heap, -heappushpop(self.min_heap, num))
        
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return float(self.min_heap[0] - self.max_heap[0]) / 2.0
        else:
            return float(self.min_heap[0])
    '''
    # Solution 2 len(max_heap) = len(min_heap) +1
    # Your runtime beats 98.72 % of python3 submissions
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = [] 
        self.min_heap = []
        
    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap): # add num to self.max_heap
            heapq.heappush(self.max_heap, -heappushpop(self.min_heap, num))
        else: # add num to self.min_heap
            heapq.heappush(self.min_heap, -heappushpop(self.max_heap, -num))
        
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return float(self.min_heap[0] - self.max_heap[0]) / 2.0
        else:
            return float(-self.max_heap[0])   


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

