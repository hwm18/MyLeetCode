#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        maxProfit, minPrice = 0, 2<<32
        for p in prices:
            minPrice = min(minPrice, p)
            maxProfit = max(maxProfit, p-minPrice)
        
        return maxProfit
            

