#
# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
#

# @lc code=start
# Your runtime beats 80.14 % of python3 submissions
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.len = k
        self.q = [None] * k
        self.front = (k - 1) % k
        self.last = 0
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.q[self.last] == None:
            self.q[self.last] = value
            self.last = (self.last + 1) % self.len
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.q[(self.front + 1) % self.len] == None:
            return False
        else:
            self.q[(self.front + 1) % self.len] = None
            self.front = (self.front + 1) % self.len
            return True


    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.q[(self.front + 1) % self.len] if self.q[(self.front + 1) % self.len] != None else -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.q[(self.last -1) % self.len] if self.q[(self.last -1) % self.len] != None else -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return (self.last - self.front) % self.len == 1 and self.q[(self.front + 1) % self.len] == None

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.last - self.front) % self.len == 1 and self.q[(self.front + 1) % self.len] != None
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

