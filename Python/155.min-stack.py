#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:        
        self.stack.append(x)
        if len(self.minStack)==0 or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
    
    ''' method 1: one stack and one min
    # Your runtime beats 93.98 % of python3 submissions
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = 1<<31

    def push(self, x: int) -> None:
        if(x<=self.min):
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.min:
            self.min = self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
    '''


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

