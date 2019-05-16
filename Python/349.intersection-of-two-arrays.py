#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
class Solution:
    # Solution 1: use set operation in python, one-line solution
    # √ Your runtime beats 99.09 % of python3 submissions
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        s1, s2=set(nums1), set(nums2)
        result = []
        for s in s1:
            if s in s2:
                result.append(s)
        return result
    """

    '''
    Solution 3:
    use dict/hashmap to record all nums appeared in the first list, and then check if there are nums in the second list have appeared in the map.
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i]+1 if i in map else 1
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] = 0
        
        return res

        Solution 4:
        sort the two list, and use two pointer to search in the lists to find common elements.
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                if not (len(res) and nums1[i] == res[len(res)-1]):
                    res.append(nums1[i])
                i += 1
                j += 1
        
        return res
        '''
