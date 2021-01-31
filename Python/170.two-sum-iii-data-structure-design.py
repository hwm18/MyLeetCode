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

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maps = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.maps:
            self.maps[number] += 1
        else:
            self.maps[number] = 1
        
    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.maps.keys():
            target = value - num
            if target == num:
                if self.maps[num] > 1:
                    return True
            elif target in self.maps:
                return True
          
        return False

        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
# @lc code=end

