#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    '''
    Accepted
    989/989 cases passed (32 ms)
    Your runtime beats 80.55 % of python3 submissions
    Your memory usage beats 97.11 % of python3 submissions (13.6 MB)
    '''
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<=1
                temp <<=1
        
        if not positive:
            res = -res
        
        return min(max(-2147483648, res), 2147483647)

# @lc code=end

