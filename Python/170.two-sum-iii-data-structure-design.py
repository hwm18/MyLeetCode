#
# @lc app=leetcode id=170 lang=python3
#
# [170] Two Sum III - Data structure design
#
# https://leetcode.com/problems/two-sum-iii-data-structure-design/description/
#
# algorithms
# Easy (34.80%)
# Likes:    371
# Dislikes: 280
# Total Accepted:    96.3K
# Total Submissions: 276.8K
# Testcase Example:  '["TwoSum","add","add","add","find","find"]\n[[],[1],[3],[5],[4],[7]]'
#
# Design a data structure that accepts a stream of integers and checks if it
# has a pair of integers that sum up to a particular value.
# 
# Implement the TwoSum class:
# 
# 
# TwoSum() Initializes the TwoSum object, with an empty array initially.
# void add(int number) Adds number to the data structure.
# boolean find(int value) Returns true if there exists any pair of numbers
# whose sum is equal to value, otherwise, it returns false.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["TwoSum", "add", "add", "add", "find", "find"]
# [[], [1], [3], [5], [4], [7]]
# Output
# [null, null, null, null, true, false]
# 
# Explanation
# TwoSum twoSum = new TwoSum();
# twoSum.add(1);   // [] --> [1]
# twoSum.add(3);   // [1] --> [1,3]
# twoSum.add(5);   // [1,3] --> [1,3,5]
# twoSum.find(4);  // 1 + 3 = 4, return true
# twoSum.find(7);  // No two integers sum up to 7, return false
# 
# 
# 
# Constraints:
# 
# 
# -10^5 <= number <= 10^5
# -2^31 <= value <= 2^31 - 1
# At most 5 * 10^4 calls will be made to add and find.
# 
# 
#

# @lc code=start
class TwoSum:
    
    # solution 1: use hashmap
    # 用HashMap来存储数据（key是num，value是num的个数）。add的时间复杂度是O(1), 
    # find的时间复杂的是O(n)，空间复杂度O(n)。 需要注意的是当在map里找到value - num时，
    # 要判断下这个值是否与num相等。如果不相等可以直接返回true，如果相等要确认num在map里不止一个
    # 17/17 cases passed (340 ms)
    # Your runtime beats 74.73 % of python3 submissions
    # Your memory usage beats 64.14 % of python3 submissions (20.5 MB)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maps = {}

    # O(1)
    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.maps[number] = self.maps.get(number, 0) + 1
    
    # solution 1: use hashmap - add O(1)  find O(n)
    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.maps.keys():
            target = value - num
            if target == num:
                if self.maps[num] > 1: # duple numbers
                    return True
            elif target in self.maps:
                return True
          
        return False


    '''
    # solution 2: use two point for find and insert soret for add
    # Time Limit Exceeded, 14/17 cases passed (N/A)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.result = []

    # insert sort: Time Limit Exceeded  O(n)
    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.result.append(number)
        index = len(self.result)-1
        while index > 0 and self.result[index-1] > self.result[index]:
            temp = self.result[index-1]
            self.result[index-1] = self.result[index]
            self.result[index] = temp
            index -= 1
                
    # solution 1: use two points  time: O(n)
    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        left, right = 0, len(self.result)-1
        while left < right:
            total = self.result[left] + self.result[right]
            if total < value:
                left +=1
            elif total > value:
                right -= 1
            else:
                return True
        
        return False
    '''
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
# @lc code=end

