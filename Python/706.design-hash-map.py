#
# @lc app=leetcode id=706 lang=python
#
# [706] Design HashMap
#
# https://leetcode.com/problems/design-hashmap/description/
#
# algorithms
# Easy (55.92%)
# Likes:    297
# Dislikes: 50
# Total Accepted:    32.5K
# Total Submissions: 58.1K
# Testcase Example:  '["MyHashMap","put","put","get","get","put","get", "remove", "get"]\n[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]'
#
# Design a HashMap without using any built-in hash table libraries.
# 
# To be specific, your design should include these functions:
# 
# 
# put(key, value) : Insert a (key, value) pair into the HashMap. If the value
# already exists in the HashMap, update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if
# this map contains no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains the
# mapping for the key.
# 
# 
# 
# Example:
# 
# 
# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);          
# hashMap.put(2, 2);         
# hashMap.get(1);            // returns 1
# hashMap.get(3);            // returns -1 (not found)
# hashMap.put(2, 1);          // update the existing value
# hashMap.get(2);            // returns 1 
# hashMap.remove(2);          // remove the mapping for 2
# hashMap.get(2);            // returns -1 (not found) 
# 
# 
# 
# Note:
# 
# 
# All keys and values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashMap library.
# 
# 
# Your runtime beats 71.11 % of python submissions
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.M = 100000
        self.arr = [None] * self.M
    
    def hash_key(self, key):
        h_key = 0
        while key > 0:
            h_key += key % self.M
            key = key / self.M
        return h_key % self.M

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        idx = self.hash_key(key)
        self.arr[idx]=value
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        idx = self.hash_key(key)
        if self.arr[idx] is None:
            return -1
        return self.arr[idx]
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        idx = self.hash_key(key)
        if self.arr[idx] is None:
            return
        self.arr[idx] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

