#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    # Solution 2: Stack
    # Your runtime beats 97.38 % of python3 submissions
    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s)==0:
            return 0
        # Input: ")()())"   stack: 3  maxLen = 4
        stack, maxLen = [], 0
        count,matchLen = 0,0
        for i in range(len(s)):
            curr = s[i]
            if curr == '(':
                stack.append(i)
            else:
                if not stack:
                    count = 0
                else:
                    matchPos = stack.pop()
                    matchLen = i - matchPos +1
                    if not stack:
                        count += matchLen
                        matchLen = count
                    else:
                        matchLen = i - stack[-1]
                maxLen = max(maxLen, matchLen)
        return maxLen


    '''
    # Solution1: 1D DP: Your runtime beats 91.73 % of python3 submissions
    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s)==0:
            return 0

        # use 1D DP
        # dp[i] records the longestValidParenthese EXACTLY ENDING at s[i]
        dp = [0 for x in range(len(s))]
        max_to_now = 0
        for i in range(1,len(s)):
            if s[i] == ')':
                # case 1: ()()
                if s[i-1] == '(':
                    # add nearest parentheses pairs + 2
                    dp[i] = dp[i-2] + 2
                # case 2: (()) 
                # i-dp[i-1]-1 is the index of last "(" not paired until this ")"
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    if dp[i-1] > 0: # content within current matching pair is valid 
                    # add nearest parentheses pairs + 2 + parentheses before last "("
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    else:
                    # otherwise is 0
                        dp[i] = 0
                max_to_now = max(max_to_now, dp[i])
        return max_to_now
    '''

# @lc code=end

