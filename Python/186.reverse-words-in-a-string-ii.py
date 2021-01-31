#
# @lc app=leetcode id=186 lang=python3
#
# [186] Reverse Words in a String II
#
# https://leetcode.com/problems/reverse-words-in-a-string-ii/description/
#
# algorithms
# Medium (45.23%)
# Likes:    542
# Dislikes: 106
# Total Accepted:    98K
# Total Submissions: 216.7K
# Testcase Example:  '["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]'
#
# Given an input string , reverse the string word by word. 
# 
# Example:
# 
# 
# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# 
# Note: 
# 
# 
# A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces.
# The words are always separated by a single space.
# 
# 
# Follow up: Could you do it in-place without allocating extra space?
# 
#

# @lc code=start
class Solution:
    '''
        18/18 cases passed (264 ms)
        Your runtime beats 51.11 % of python3 submissions
        Your memory usage beats 91.8 % of python3 submissions (19 MB)
    '''
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s or len(s)==0:
            return
        
        ln = len(s)
        self.reverse(s, 0, ln-1)
        print(s)
        start = 0
        for end in range(ln):
           if(end == ln-1):
               self.reverse(s, start, end)
           elif(s[end] == ' '):
                self.reverse(s, start, end-1)
                start = end + 1
    
    def reverse(self, s, start, end):
        while start<end:
            s[start], s[end] = s[end], s[start]
            start +=1
            end -= 1
        
# @lc code=end

