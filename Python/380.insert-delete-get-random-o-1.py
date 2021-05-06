#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
#
# algorithms
# Medium (48.68%)
# Likes:    3553
# Dislikes: 207
# Total Accepted:    334.5K
# Total Submissions: 679.6K
# Testcase Example:  '["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]\n' +
  '[[],[1],[2],[2],[],[1],[2],[]]'
#
# Implement the RandomizedSet class:
# 
# 
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns
# true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns
# true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements
# (it's guaranteed that at least one element exists when this method is
# called). Each element must have the same probability of being returned.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove",
# "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]
# 
# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was
# inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now
# contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2
# randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now
# contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set,
# getRandom() will always return 2.
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= val <= 2^31 - 1
# At most 10^5 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is
# called.
# 
# 
# 
# Follow up: Could you implement the functions of the class with each function
# works in average O(1) time?
#

# @lc code=start
class RandomizedSet:
    '''
    使用数组来保存当前集合中的元素，同时用一个hashMap来保存数字与它在数组中下标的对应关系。
    插入操作时：
    若已存在此元素返回false
    不存在时将新的元素插入数组最后一位，同时更新hashMap。

    删除操作时：
    若不存在此元素返回false
    存在时先根据hashMap得到要删除数字的下标，再将数组的最后一个数放到需要删除的数的位置上，删除数组最后一位，同时更新hashMap。
    
    获取随机数操作时：
    根据数组的长度来获取一个随机的下标，再根据下标获取元素。
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.val2idx = [], {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val2idx:
            return False
        
        self.nums.append(val)
        self.val2idx[val] = len(self.nums)-1
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val2idx:
            return False
        
        index = self.val2idx[val]
        lastVal = self.nums[-1]

        # move the last element to index
        self.nums[index] = lastVal
        self.val2idx[lastVal] = index

        # remove the last element
        self.nums.pop()
        del self.val2idx[val]
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0,len(self.nums)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

