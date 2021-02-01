#
# @lc app=leetcode id=159 lang=python3
#
# [159] Longest Substring with At Most Two Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/
#
# algorithms
# Medium (50.35%)
# Likes:    1216
# Dislikes: 21
# Total Accepted:    135.8K
# Total Submissions: 269.7K
# Testcase Example:  '"eceba"'
#
# Given a string s , find the length of the longest substring t  that contains
# at most 2 distinct characters.
# 
# Example 1:
# 
# 
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
# 
# 
# Example 2:
# 
# 
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.
# 
# 
#

# @lc code=start
class Solution:
    '''
    125/125 cases passed (56 ms)
    Your runtime beats 66.89 % of python3 submissions
    Your memory usage beats 92.83 % of python3 submissions (14.2 MB)
    '''
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s or len(s)==0:
            return 0
        
        ln=len(s)
        i,ans,distinct = 0,0,0
        count = {}
        for j in range(ln):
            c = s[j]
            if c not in count or count[c]==0:
                distinct +=1
            count[c] = count.get(c,0) + 1
            while(distinct >2):
                count[s[i]] = count.get(s[i], 0) - 1
                if(count[s[i]] == 0):
                    distinct -=1
                i += 1
            ans = max(ans, j-i+1)

        return ans

        
# @lc code=end

