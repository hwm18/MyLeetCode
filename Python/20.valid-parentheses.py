#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    # Your runtime beats 95.13 % of python3 submissions
    def isValid(self, s: str) -> bool:
        if not s or len(s)==0:
            return True
        
        maps = {')':'(',']':'[','}':'{'}
        stack = []
        for ss in s:
            if ss in maps:                
                if not (stack and stack.pop()== maps[ss]):
                    return False
            else:
                stack.append(ss)
        
        return len(stack)==0

            


# @lc code=end

