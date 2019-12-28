#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (43.87%)
# Total Accepted:    382.9K
# Total Submissions: 872.8K
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# Note: Given n will be a positive integer.
# 
# Example 1:
# 
# 
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
#
class Solution(object):
    '''
    # Solution 3: Time Limit Exceeded - 10/45 cases passed (N/A)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int        
        """
        if n ==0 or n==1:
            return 1
        catch = [ 0 for _ in range(n+1)]
        catch[0]= 1
        catch[1] = 1
        #catch[2] = 2
        for i in range(2, n+1):
            if catch[i] != 0:
                return catch[i]
           
            catch[i] = self.climbStairs(i-1) + self.climbStairs(i-2)
        return catch[n]
    '''

    '''
    考虑最后一步走1阶还是走2阶。
    方案数Dp[n] = 最后一步走1阶的方案数 + 最后一步走2阶的方案数。
    Dp[n] = Dp[n-1] + Dp[n-2].
    '''
    '''
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n==0):
            return 1
        
        if(n<=2):
            return n
        # Your runtime beats 70.5 % of python submissions
        f =[1,2]
        for i in range(n-2):
            f.append(f[-1] + f[-2])
        
        return f[-1]
    '''

    # Your runtime beats 88.69 % of python submissions
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n == 0 or n == 1):
            return 1
                
        f = [1,1]        
        for _ in range(2,n+1):
            f.append(f[-1] + f[-2])
        
        return f[-1]


        

