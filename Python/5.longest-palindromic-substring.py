#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (29.54%)
# Likes:    8157
# Dislikes: 579
# Total Accepted:    1.1M
# Total Submissions: 3.5M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# Example 3:
# 
# 
# Input: s = "a"
# Output: "a"
# 
# 
# Example 4:
# 
# 
# Input: s = "ac"
# Output: "a"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),
# 
# 
#

# @lc code=start
class Solution:
    # solution 2： DP
    '''
    解题思路
    由回文串正序和反序的性质相同，可以得出一个性质，如果一个字符串，其中心不是回文串，那么它一定不是个回文串。如果去掉头和尾，它依然还是一个回文串。在头和尾加上同一个字符也是一个回文串。
    由此可以得出判断一个区间是否是回文串，可以由更小的区间得到，并且不受包含这个区间的大区间影响，所以满足无后效性且是最有子结构，可以用动态规划求解。

    代码思路
    动态规划
    设dp(l, r)，代表区间[l, r]是否是回文串。
    如果s[l] == s[r]，并且s[l + 1 ~ r - 1]是回文串的话，s[l ~ r]就是回文串。

    复杂度分析
    设字符串长度为 N。
    时间复杂度
    枚举端点，O(1)时间转移，时间复杂度为O(n^2)。
    空间复杂度
    需要额外O(n^2)空间记录dp值。
    '''
    def longestPalindrome(self, s: str) -> str:
         # 重点1：任何代码都要进行异常检测
        if not s:
            return ""
        
        length = len(s)
        max_len = 1
        start = 0
        is_palindrome = [[False] * length for _ in range(length)]
        
        # 将长度为 1 的 dp 值设为真
        for i in range(length):
            is_palindrome[i][i] = True
        
        for i in range(length - 1):
            if s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = True
                max_len = 2
                start = i
        
        for new_len in range(3, length + 1):
            for left in range(length - new_len + 1):
                right = left + new_len - 1
                if is_palindrome[left + 1][right - 1] and s[left] == s[right]:
                    is_palindrome[left][right] = True
                    # 更新答案
                    if new_len > max_len:
                        max_len = new_len
                        start = left
        
        return s[start : start + max_len]


    '''
    # solution 1: 基于中心点枚举的算法，时间复杂度 O(n^2)
    # 176/176 cases passed (956 ms)
    # Your runtime beats 77.07 % of python3 submissions
    # Your memory usage beats 31.54 % of python3 submissions (14.2 MB)
    def longestPalindrome(self, s: str) -> str:
         # 重点1：任何代码都要进行异常检测
        if not s:
            return ""
        
        # 重点2：用空行区分开异常检测部分，核心代码部分，和返回值部分，属于高端代码风格技巧
        res = ""
        # time: O(N^2)
        for i in range(len(s)):
            #  重点3：子函数化避免重复代码
            # odd case, like "aba"
            tmp = self.helper(s,i,i)
            # 重点4：通过返回值来避免使用全局变量这种不好的代码风格
            if len(tmp) > len(res):
                res = tmp
            
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        
        # 重点2：用空行区分开异常检测部分，核心代码部分，和返回值部分，属于高端代码风格技巧
        return res
    
    # two points check 一个字符串是否是回文，复杂度为 O(N)
    def helper(self, s, left, right):
        while left>=0 and right<len(s)
            # 重点5：将复杂判断拆分到 while 循环内部，而不是放在 while 循环中，提高代码可读性
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        
        return s[left+1: right]
    '''
    
        
# @lc code=end

