#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    # Your runtime beats 93.81 % of python3 submissions
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens or len(tokens)==0:
            return 0
        
        stack =[]
        for item in tokens:
            if item not in '+-*/':
                stack.append(int(item))
            else:
                a = stack.pop()
                b = stack.pop()
                temp = 0
                if item =='+':
                    temp = a + b
                elif item =='-':
                    temp = b - a
                elif item =='*':
                    temp = a * b
                else:
                    # here take care of the case like "1/-22",
                    # in Python 2.x, it returns -1, while in 
                    # Leetcode it should return 0
                    temp = b // a
                    if b * a < 0 and b % a !=0:
                        temp += 1

                stack.append(temp)
        
        return stack.pop()

                


# @lc code=end

