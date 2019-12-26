#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    '''
    # Solution 1: Your runtime beats 27.18 % of python3 submissions
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums)==0:
            return []
        
        queue = collections.deque()
        results = []
        for num in nums:
            queue.append(num)
            # l = len(queue)
            if len(queue)<k:
               continue
            else:
                results.append(max(queue))
                queue.popleft()
        return results
    '''

    # solution 2: Your runtime beats 94.14 % of python3 submissions
    # Keep indexes of good candidates in deque d. The indexes in d are from the current window, they’re increasing,
    # and their corresponding nums are decreasing. Then the first deque element is the index of the largest 
    # window value.
    # For each index i:
    # Pop (from the end) indexes of smaller elements (they’ll be useless).
    # Append the current index.
    # Pop (from the front) the index i - k, if it’s still in the deque (it falls out of the window).
    # If our window has reached size k, append the current window maximum to the output.
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums)==0:
            return []
        
        d = collections.deque()
        results = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()   # Pop (from the end) indexes of smaller elements (they’ll be useless).
            
            d.append(i) # Append the current index.
            if d[0] == i -k:
                d.popleft()  # Pop (from the front) the index i - k, if it’s still in the deque (it falls out of the window)
            if i >= k-1:
                results.append(nums[d[0]])  #  reached size k, append the current window maximum to the output
        return results

# @lc code=end

