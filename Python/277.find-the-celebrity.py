#
# @lc app=leetcode id=277 lang=python
#
# [277] find-the-celebrity
#
# https://www.lintcode.com/problem/find-the-celebrity/description
#
# Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.
# Now you want to find out who the celebrity is or verify that there is not one. 
# The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" 
# to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) 
# by asking as few questions as possible (in the asymptotic sense).

# You are given a helper function bool knows(a, b) which tells you whether A knows B. 
# Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.
# Example1
# Input:
# 2 // next n * (n - 1) lines 
# 0 knows 1
# 1 does not know 0
# Output: 1
# Explanation:
# Everyone knows 1,and 1 knows no one.

# Example2
# Input:
# 3 // next n * (n - 1) lines 
# 0 does not know 1
# 0 does not know 2
# 1 knows 0
# 1 does not know 2
# 2 knows 0
# 2 knows 1
# Output: 0
# Explanation:
# Everyone knows 0,and 0 knows no one.
# 0 does not know 1,and 1 knows 0.
# 2 knows everyone,but 1 does not know 2.
# Your submission beats 34.43% Submissions!
"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""
class Solution:
    # Your submission beats 65.31% Submissions!
    def findCelebrity(self, n):
        # @param {int} n a party with n people
        # @return {int} the celebrity's label or -1
        if n == 0:
            return -1
        if n == 1:
            return 0
        
        label = 0
        for i in range(1, n):
            if Celebrity.knows(label, i):
                label = i
        
        # verify label is Celebrity or not
        for i in range(0, n):
            if i!=label and Celebrity.knows(label, i):
                return -1
            if i!=label and not Celebrity.knows(i, label):
                return -1
        
        return label
            

        

