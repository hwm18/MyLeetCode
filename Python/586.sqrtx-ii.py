#
# @lc app=lintcode id=586 lang=python
#
# [586] Sqrt(x)
#
# https://www.lintcode.com/problem/sqrtx-ii/description

# Implement double sqrt(double x) and x >= 0.
# Compute and return the square root of x.
# Example 1:
# Input: n = 2 
# Output: 1.41421356

# Example 2:
# Input: n = 3
# Output: 1.73205081
#
class Solution(object):
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        if x ==0 or x == 1:
            return x
        
        result = 1.0
        while(abs(x -result * result) > 1e-12):
            result = (result + x/result)/2
            
        return result

        

