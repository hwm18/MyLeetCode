#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (28.41%)
# Likes:    5595
# Dislikes: 313
# Total Accepted:    941.9K
# Total Submissions: 3.3M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#
class Solution(object):
    # solution 4: two points - Your runtime beats 93.13 % of python submissions
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window_start = 0
        max_length = 0
        char_index_map = {}

        # try to extend the range [windowStart, windowEnd]
        for window_end in range(len(s)):
            right_char = s[window_end]
            # if the map already contains the 'right_char', shrink the window from the beginning so that
            # we have only one occurrence of 'right_char'
            if right_char in char_index_map:
                # this is tricky; in the current window, we will not have any 'right_char' after its previous index
                # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
                window_start = max(window_start, char_index_map[right_char] + 1)
            # insert the 'right_char' into the map
            char_index_map[s[window_end]] = window_end
            # remember the maximum length so far
            max_length = max(max_length, window_end - window_start + 1)
        return max_length

    '''
    # solution 3: two points - Your runtime beats 43.25 % of python submissions
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        start = 0
        ans = 0
        for end in range(len(s)):
            c = s[end]
            d[c] = d.get(c,0)+1

            while d[c]>1:
                d[s[start]] -=1
                if d[s[start]] == 0:
                    del d[s[start]]
                start += 1
            
            ans = max(ans, end - start +1)

        return ans
    '''

    '''
    # solution 2: Your runtime beats 98.97 % of python submissions
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        start = ans = 0
        usedChar = {}
        for i,c in enumerate(s):
            if c in usedChar and start <=usedChar[c]:
                start = usedChar[c] + 1
            else:
                ans = max(ans, i - start + 1)
            usedChar[c] = i

        return ans
    '''

    '''
    # solution 1: Your runtime beats 8 % of python submissions
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        ans = 0
        
        #i,j=0,0
        for i in range(len(s)):
            d = set(s[i])
            j = i+1
            while j<len(s) and s[j] not in d:
                d.add(s[j])
                j +=1
            ans = max(ans, len(d))
        return ans
    '''
            
            
                
        

