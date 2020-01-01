#
# @lc app=leetcode id=457 lang=python3
#
# [457] Circular Array Loop
#

# @lc code=start
class Solution:
    # Solution 1: Your runtime beats 48.5 % of python3 submissions
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if not nums or len(nums)==0:
            return False
        
        n = len(nums)
        s = []
        for i, val in enumerate(nums):
            if i in s: continue   # check repeated i
            d = []
            while val * nums[i] >0:  # forward or backward movements only
                if i in d:
                    if d[-1] !=i:
                        return True   # the cycle's length must be greater than 1
                    else:
                        break
                d.append(i)    # store i for a cycle
                s.append(i)    # store i without checking the repetition in the following
                i = (i + nums[i]) % n
        return False
    
    # solution 2:  Wrong Answer - 34/42 cases passed (N/A) Test case: [1,1,2] Answer: false  Expected Answer: True
    # From here - incorrect: https://www.jiuzhang.com/solution/circular-array-loop/#tag-highlight-lang-java
    # def circularArrayLoop(self, nums: List[int]) -> bool:
    #     if not nums or len(nums)==0:
    #         return False
        
    #     n = len(nums)
    #     for i in range(n):
    #         curr = nums[i]
    #         nums[i] = 0
    #         if curr == 0:
    #             continue  # visited
            
    #         next = (i + curr + n)% n
    #         if next == i:
    #             continue  # loop back to self not more than one

    #         while curr * nums[next] > 0: # make sure same direction and meet visited it will stop
    #             curr = nums[next]
    #             nums[next] = 0
    #             next = (curr + next + n) %n
            
    #         if i == next:
    #             return True

    #     return False
        
# @lc code=end

