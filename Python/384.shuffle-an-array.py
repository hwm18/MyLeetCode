#
# @lc app=leetcode id=384 lang=python3
#
# [384] Shuffle an Array
#
class Solution:
    #Your runtime beats 55.44 % of python3 submissions
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.init_nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.init_nums
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        return random.sample(self.nums, len(self.nums))


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

