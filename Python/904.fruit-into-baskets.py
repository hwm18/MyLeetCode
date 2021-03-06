#
# @lc app=leetcode id=904 lang=python
#
# [904] Fruit Into Baskets
#
# https://leetcode.com/problems/fruit-into-baskets/description/
#
# algorithms
# Medium (41.46%)
# Likes:    456
# Dislikes: 687
# Total Accepted:    54.8K
# Total Submissions: 132.1K
# Testcase Example:  '[1,2,1]'
#
# In a row of trees, the i-th tree produces fruit with type tree[i].
# 
# You start at any tree of your choice, then repeatedly perform the following
# steps:
# 
# 
# Add one piece of fruit from this tree to your baskets.  If you cannot,
# stop.
# Move to the next tree to the right of the current tree.  If there is no tree
# to the right, stop.
# 
# 
# Note that you do not have any choice after the initial choice of starting
# tree: you must perform step 1, then step 2, then back to step 1, then step 2,
# and so on until you stop.
# 
# You have two baskets, and each basket can carry any quantity of fruit, but
# you want each basket to only carry one type of fruit each.
# 
# What is the total amount of fruit you can collect with this procedure?
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,1]
# Output: 3
# Explanation: We can collect [1,2,1].
# 
# 
# 
# Example 2:
# 
# 
# Input: [0,1,2,2]
# Output: 3
# Explanation: We can collect [1,2,2].
# If we started at the first tree, we would only collect [0, 1].
# 
# 
# 
# Example 3:
# 
# 
# Input: [1,2,3,2,2]
# Output: 4
# Explanation: We can collect [2,3,2,2].
# If we started at the first tree, we would only collect [1, 2].
# 
# 
# 
# Example 4:
# 
# 
# Input: [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can collect [1,2,1,1,2].
# If we started at the first tree or the eighth tree, we would only collect 4
# fruits.
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= tree.length <= 40000
# 0 <= tree[i] < tree.length
# 
# 
#
class Solution(object):
    '''
    # solution 1: slide window - Your runtime beats 51.16 % of python submissions
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        start = 0
        count = {}
        ans = 0
        for end, fruite in enumerate(tree):
            count[fruite] = count.get(fruite, 0) + 1
        
            while len(count) > 2:
                count[tree[start]] -=1
                if count[tree[start]] ==0:
                    del count[tree[start]]
                start +=1
            ans = max(ans, end - start +1)

        return ans
    '''

    # Solution 2:  Your runtime beats 93.58 % of python submissions
    # I have 2 baskets b1 and b2 with the count of fruits b1N, b2N
    # If I encounter a fruit b2 (which is the “front” basket), I simply add it to the basket.
    # If I encounter a fruit b1, I swap the baskets and update the counts.
    # If I encounter a different fruit, I drop the basket b1 and b2 becomes the new b1. In this case, 
    # the new count b1N will be only b2NCons (which was the count of consecutive b2)
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """ 
        b1, b2, b1N, b2N, b2NCons, maxPick = None, None, 0, 0, 0, 0

        for fruit in tree:
            if fruit == b2:
                b2N, b2NCons = b2N + 1, b2NCons + 1

            elif fruit == b1:
                b1, b2, b1N, b2N, b2NCons = b2, b1, b2N, b1N+1, 1

            else:
                b1, b2, b1N, b2N, b2NCons = b2, fruit, b2NCons, 1, 1

            maxPick = max(maxPick, b1N+b2N)

        return maxPick

