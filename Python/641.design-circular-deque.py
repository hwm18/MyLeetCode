#
# @lc app=leetcode id=641 lang=python3
#
# [641] Design Circular Deque
#

# @lc code=start

# Solution 2: Your runtime beats 84.06 % of python3 submissions
# self.front is the index before the start of queue. self.last is the index after the end of the queue
# list index    0, 1, 2, 3, 4, 5
# queue squence 1, 2, 3, 4, 5, 6
# self.front = 5
# self.last = 1

# list index    0, 1, 2, 3, 4, 5
# queue squence 5, 6, 1, 2, 3, 4
# self.front = 1
# self.last = 2
class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.len = k
        self.q = [None] * k
        self.front = (k - 1) % k
        self.last = 0
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.q[self.front] == None:
            self.q[self.front] = value
            self.front = (self.front - 1) % self.len
            return True
        else:
            return False
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.q[self.last] == None:
            self.q[self.last] = value
            self.last = (self.last + 1) % self.len
            return True
        else:
            return False
        

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.q[(self.front + 1) % self.len] == None:
            return False
        else:
            self.q[(self.front + 1) % self.len] = None
            self.front = (self.front + 1) % self.len
            return True
        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.q[(self.last - 1) % self.len] == None:
            return False
        else:
            self.q[(self.last - 1) % self.len] = None
            self.last = (self.last - 1) % self.len
            return True
        

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        return self.q[(self.front + 1) % self.len] if self.q[(self.front + 1) % self.len] != None else -1
        

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        return self.q[(self.last -1) % self.len] if self.q[(self.last -1) % self.len] != None else -1
        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return (self.last - self.front) % self.len == 1 and self.q[(self.front + 1) % self.len] == None
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return (self.last - self.front) % self.len == 1 and self.q[(self.front + 1) % self.len] != None
        

'''
# Solution 1: use an array [] 
# Your runtime beats 84.06 % of python3 submissions
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.k = k
        self.deque = []
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.deque)==self.k:
            return False
        self.deque.insert(0,value)
        return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.deque)==self.k:
            return False
        self.deque.append(value)
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.deque)==0:
            return False
        self.deque.remove(self.deque[0])
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.deque)==0:
            return False
        self.deque.pop()
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if len(self.deque)==0:
            return -1
        return self.deque[0]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if len(self.deque)==0:
            return -1
        return self.deque[-1]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return len(self.deque)==0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.deque)==self.k
'''

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

