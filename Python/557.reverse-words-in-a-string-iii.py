#
# @lc app=leetcode id=557 lang=python
#
# [557] Reverse Words in a String III
#
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (64.04%)
# Likes:    615
# Dislikes: 66
# Total Accepted:    125.1K
# Total Submissions: 195.3K
# Testcase Example:  '"Let\'s take LeetCode contest"'
#
# Given a string, you need to reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order.
# 
# Example 1:
# 
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# 
# 
# 
# Note:
# In the string, each word is separated by single space and there will not be
# any extra space in the string.
# 
#
class Solution(object):
    # solution 2: # s.split(' ') creates a list of words, list comprehension diverts symbols within a word and ' '.join() joins them back into a string
    # def reverseWords(self, s):
	# 	return ' '.join([word[::-1] for word in s.split(' ')])     
        
    # solution 1: Your runtime beats 14.33 % of python submissions
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s)==0:
            return s
        
        word = ""
        answer = ""
        for c in s:
            if c == ' ':
                if word != "":
                    answer += word[::-1]
                word = ""
                answer += c
            else:
                word += c

        if word != "":
            answer += word[::-1]
        return answer
    

