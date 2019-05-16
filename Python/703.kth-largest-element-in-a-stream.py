#
# @lc app=leetcode id=703 lang=python
#
# [703] Kth Largest Element in a Stream
#
# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
#
# algorithms
# Easy (46.13%)
# Likes:    289
# Dislikes: 127
# Total Accepted:    31.3K
# Total Submissions: 67.8K
# Testcase Example:  '["KthLargest","add","add","add","add","add"]\n[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]'
#
# Design a class to find the kth largest element in a stream. Note that it is
# the kth largest element in the sorted order, not the kth distinct element.
#
# Your KthLargest class will have a constructor which accepts an integer k and
# an integer array nums, which contains initial elements from the stream. For
# each call to the method KthLargest.add, return the element representing the
# kth largest element in the stream.
#
# Example:
#
#
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
#
#
# Note:
# You may assume that nums' length ≥ k-1 and k ≥ 1.
#
#
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.count = 1
        self.left = None
        self.right = None


class KthLargest(object):
    # soluiton 2: min heap
    # 这题可以使用最小堆，保持堆的大小是k，顶部就是第k大的数。时间复杂度是o(nlogk)
    # Your runtime beats 62.28 % of python submissions
    import heapq

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = []
        for n in nums:
            self.add(n)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif self.heap[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        return self.heap[0]

    ''' 
    #Solution 1: use BST - can't submit as Time Limit Exceeded
    #description is here:
    #https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/142/conclusion/1009/
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.root = None
        self.k = k
        for num in nums:
            self.addNode(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.addNode(val)
        return self.findKthLargest()

    def findKthLargest(self):
        cnt, walker = self.k, self.root
        while cnt > 0:
            pos = 1 + (walker.right.count if walker.right else 0)
            if cnt == pos:
                break
            if cnt > pos:
                cnt -= pos
                walker = walker.left
            else:
                walker = walker.right
        return walker.val

    def addNode(self, val):
        # root.count +=1
        # if root.val < val:
        #     root.right = self.addNode(root.right, val)
        # else:
        #     root.left = self.addNode(root.left, val)
        # return root
        prev = None
        curr = self.root
        while curr:
            prev = curr
            curr.count += 1
            # cur = (val < cur.val) ? cur.left : cur.right;
            curr = curr.left if (val < curr.val) else curr.right

        curr = TreeNode(val)
        if prev is None:
            self.root = curr
        else:
            if val < prev.val:
                prev.left = curr
            else:
                prev.right = curr
    '''


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

