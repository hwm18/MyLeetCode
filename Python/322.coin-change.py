#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    # soluton DP: dp[len(coins)][amount] Your runtime beats 39.99 % of python3 submissions
    # 这是一个典型的完全背包问题。
    # 设dp[i][j]表示使用前i个硬币，总金额为j时需要的最少硬币数量。
    # dp[i][j]=max(dp[i-1][j],dp[i-1][j-k*coin[i]]+k) (0≤k*coin[i]≤j)
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = 100000000000000
        ans = [MAX for i in range(amount + 1)]
        ans[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                ans[i] = min(ans[i], ans[i - coin] + 1)

        if ans[amount] == MAX:
            return -1

        return ans[amount]

    '''
    # Solution 2: BFS - Your runtime beats 94.35 % of python3 submissions
    # This solution is inspired by the BFS solution for problem Perfect Square.
    # Since it is to find the least coin solution (like a shortest path from 0 to amount), using BFS gives results much faster than DP.
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount ==0:
            return 0
        
        value1, value2=[0],[]
        count = 0
        visited = [False] * (amount + 1)
        visited[0]=True
        while  value1:
            count += 1
            for v in value1:
                for coin in coins:
                    newVal = v + coin
                    if newVal == amount:
                        return count
                    elif newVal > amount:
                        continue
                    elif not visited[newVal]:
                        visited[newVal] = True
                        value2.append(newVal)
            
            value1,value2=value2,[]
        
        return -1
    '''

# @lc code=end

