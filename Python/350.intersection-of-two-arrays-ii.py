#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        # method 2
        cnt, result = {}, []
        for n in nums1:
            if n not in cnt:
                cnt[n] =1
            else:
                cnt[n] +=1
            
        for m in nums2:
            if m in cnt and cnt[m] >0:
                result.append(m)
                cnt[m] -=1
            
        return result


        ''' method 1
        nums1.sort()
        nums2.sort()
        i,j=0,0
        result = []
        while i< len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i +=1
            elif nums1[i] > nums2[j]:
                j +=1
            else:
                result.append(nums1[i])
                i +=1
                j +=1
        
        return result
        '''


