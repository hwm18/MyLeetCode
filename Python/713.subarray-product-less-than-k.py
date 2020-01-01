#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    '''
    # Solution 1: O(n2) LTE
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums or len(nums)==0:
            return 0
        
        n = len(nums)
        count = 0
        for i in range(n):
            curr = nums[i]
            if curr >= k:
                continue

            if curr < k:  # 1 number
                count += 1
            
            result = curr
            for j in range(i+1, n):
                result *= nums[j]
                if result>= k:
                    break
                else:
                    count += 1
        return count
    '''
    '''
    # solution 2: O(n) - Your runtime beats 72.88 % of python3 submissions
    # Test case: [10,5,2,6] 100
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums or len(nums)==0:
            return 0
        
        status = (1, 0)  # (product of elements in window, left window)
        result = 0
        for i, num in enumerate(nums): # (0,10)  (1,5)   (2,2)     (3,6)
            product, left = status   #   (1,0)    (10,0)  (50,0)   (10,1)
            product *= num           #   10        50     100      60
            while product >= k and left < i+1:
                product //= nums[left]      #              10    
                left += 1                    #             1

            status = (product, left)  #  (10,0)    (50,0)  (10,1) (60,1)
            result += i - left + 1    #  1           3      5       8
        
        return result   # 8

    '''

    # Soluiton 3: Your runtime beats 51.62 % of python3 submissions
    # 维护一个滑动窗口，left为窗口的左端点，i用来探索下一个数，left和i组成的滑动窗口为[left, i]
    # 如果当前窗口中的所有数的乘积 >= k， 说明窗口不再满足条件( < k), 则把left指向的左端点的数从窗口中去掉，反映在窗口乘积上应该是除以要删除的这个数，然后left++，一直重复下去直到窗口再次满足条件，则又找到了一个新的窗口，窗口的长度就是当前窗口中满足条件的子数组个数，
    # 窗口长度用 i - left + 1来表示。
    # 时间复杂度为O(n)
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums or len(nums)==0:
            return 0
        
        product, left, result = 1,0,0
        for i, num in enumerate(nums):
            product *= num
            while left <=i and product>=k:
                product //= nums[left]
                left += 1
                
            result += i - left + 1
        
        return result
            

        
# @lc code=end

