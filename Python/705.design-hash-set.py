#
# @lc app=leetcode id=705 lang=python
#
# [705] Design HashSet
#
# https://leetcode.com/problems/design-hashset/description/
#
# algorithms
# Easy (53.47%)
# Likes:    128
# Dislikes: 36
# Total Accepted:    20.5K
# Total Submissions: 38.4K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# Design a HashSet without using any built-in hash table libraries.
# 
# To be specific, your design should include these functions:
# 
# 
# add(value): Insert a value into the HashSet. 
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in
# the HashSet, do nothing.
# 
# 
# 
# Example:
# 
# 
# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);         
# hashSet.add(2);         
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);          
# hashSet.contains(2);    // returns true
# hashSet.remove(2);          
# hashSet.contains(2);    // returns false (already removed)
# 
# 
# 
# Note:
# 
# 
# All values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashSet library.
# 
# 
# Your runtime beats 73.92 % of python submissions
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.M = 10000
        self.arr = [None] * self.M

    def hash_key(self, key):
        h_key = 0
        while key > 0:
            h_key += key % self.M
            key = key / self.M
        return h_key % self.M

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        idx = self.hash_key(key)
        while self.arr[idx] is not None:
            idx = (idx +1) % self.M
        self.arr[idx] = key

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        idx = self.hash_key(key)
        if self.arr[idx] is None:
            return
        
        while self.arr[idx] is not None:
            if self.arr[idx] != key:
                idx = (idx +1) %self.M
            else:
                # keep searching in case earlier collision was deleted
                self.arr[idx] = -1
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        idx = self.hash_key(key)
        if self.arr[idx] is None:
            return False

        while self.arr[idx] is not None:
            if self.arr[idx] != key:
                idx = (idx +1) % self.M
            else:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

