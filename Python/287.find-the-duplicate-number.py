#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#
class Solution(object):
    # Solution 2: Your runtime beats 29.62 % of python submissions
    # 这个题比较好的理解方法是画一个坐标轴：
    # x轴是 0, 1, 2, ... n。
    # y轴是对应的 <=x 的数的个数，比如 <=0 的数的个数是0，就在（0,0）这个坐标画一个点。
    # <=n 的数的个数是 n+1 个，就在 (n,n+1)画一个点。
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)<2:
            return -1
        
        start,end=1, len(nums)-1
        while start + 1 < end:
            mid = start + (end-start)//2
            if self.count_smaller_equal(nums,mid) > mid:
                end = mid
            else:
                start = mid

        if self.count_smaller_equal(nums,start)>start:
            return start
        return end

    def count_smaller_equal(self, nums,val):
        cnt=0
        for n in nums:
            if n<=val:
                cnt+=1
        return cnt
    
    '''
    # Solution 1: Your runtime beats 60.87 % of python submissions
    # In this problem, nums[a] = b can be seen as a.next = b, 
    # the the problem is exactly the same as Linked List Cycle II 
    # which finds the node that cycle begins.
    # Example: [3,1,3,4,2] -> output: 3
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast, finder=0,0,0
        while True:                 # Example: [3,1,3,4,2] -> output: 3
            slow = nums[slow]       # nums[0]=3 -> nums[3]=4 -> nums[4]=2
            fast = nums[nums[fast]] # nums[3]=4 -> nums[2]=3 -> nums[4]=2
            if slow == fast:  # slow=fast=2
                while finder != slow:  # finder=0, slow=2 -> finder=3,slow=3
                    finder = nums[finder]
                    slow = nums[slow]
                return finder
       '''

        

        

