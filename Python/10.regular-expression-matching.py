#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
     # Solution 2: DP - Your runtime beats 69.03 % of python3 submissions
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for i in range(0,len(p) + 1)] for j in range(0, len(s) + 1)]
        dp[0][0] = True   #dp[0][0]初始化为true，由此开始转移
        for i in range(1, len(p) + 1):
            if (p[i - 1] == '*'):		
                dp[0][i] = dp[0][i - 2] # '*'不去匹配

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':      #'*'不去匹配
                    dp[i][j] = dp[i][j - 2] 
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.': 
                        dp[i][j] |= dp[i-1][j]
                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':  #如果两字符相同或者为.
                        dp[i][j] = dp[i - 1][j - 1]    #当前状态由前一个转移而来
    
        return dp[len(s)][len(p)]
    '''
    # solution 1: momery search - Your runtime beats 96.51 % of python3 submissions
    def isMatch(self, s: str, p: str) -> bool:
        if not p or len(p)==0:
            return not s
        
        return self.helper(s,0,p,0,{})
    '''
    # solution 1: momery search - Your runtime beats 96.51 % of python3 submissions
    def helper(self, s, i, p, j, memo):
        if (i,j) in memo:
           return memo[(i,j)]
        
        # s is empty
        if len(s)==i:
            return self.is_empty(p[j:])
        
        if len(p)==j: # p is end, but s isn't end
            return False

        if j+1< len(p) and p[j+1]=='*': # 如果为'*'，有两种方案
            # *'重复前面一个字符去匹配s (i+1) or '*' 不去匹配 (j+2)
            matched = self.is_match_char(s[i],p[j]) and self.helper(s,i+1,p,j, memo) or self.helper(s, i, p,j+2, memo)  
        else:
            matched = self.is_match_char(s[i],p[j]) and self.helper(s,i+1,p,j+1,memo)

        memo[(i,j)] = matched
        return matched
            
        
    def is_match_char(self, s, p):  # 判断两字符是否匹配
        return s == p or p == '.'
        
    def is_empty(self, pattern): # 形如"x*x*"形式
        if len(pattern) % 2 == 1: # 如果不是'*'，无法匹配
            return False
        
        for i in range(len(pattern) // 2):
            if pattern[i * 2 + 1] != '*': # 如果不是'*'，无法匹配
                return False
        return True

# @lc code=end

