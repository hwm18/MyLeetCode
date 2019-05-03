#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        profit, i = 0, n-1
        while i >0:
            sell = prices[i]
            buy = prices[i-1]
            if(sell > buy):
                profit += (sell - buy)
            i -= 1
            
        return profit

