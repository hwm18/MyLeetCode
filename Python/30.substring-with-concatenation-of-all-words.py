#
# @lc app=leetcode id=30 lang=python
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (23.69%)
# Likes:    527
# Dislikes: 907
# Total Accepted:    135.1K
# Total Submissions: 570.4K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
# 
# Example 1:
# 
# 
# Input:
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
# 
# 
# Example 2:
# 
# 
# Input:
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# Output: []
# 
# 
#
class Solution(object):
    '''
    # solution: slid-window: Your runtime beats 45.83 % of python submissions
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0 or len(words[0]) == 0:
            return []

        word_frequency = {}
        for word in words:
            if word not in word_frequency:
                word_frequency[word] = 0
            word_frequency[word] += 1

        result_indices = []
        words_count = len(words)
        word_length = len(words[0])
        for i in range((len(s) - words_count * word_length)+1):
            words_seen = {}
            for j in range(0, words_count):
                next_word_index = i + j * word_length
                # Get the next word from the string
                word = s[next_word_index: next_word_index + word_length]
                if word not in word_frequency:  # Break if we don't need this word
                    break

                # Add the word to the 'words_seen' map
                if word not in words_seen:
                    words_seen[word] = 0
                words_seen[word] += 1

                # No need to process further if the word has higher frequency than required
                if words_seen[word] > word_frequency.get(word, 0):
                    break

                if j + 1 == words_count:  # Store index if we have found all the words
                    result_indices.append(i)                

        return result_indices
    '''
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words)==0 or len(words[0]) ==0:
            return []
        
        word_map={}
        ans = []

        for word in words:
            word_map[word] = word_map.get(word,0) +1

        word_count, word_len = len(words), len(words[0])
        for i in range((len(s) - word_count * word_len)+1):
            see = {}
            for j in range(word_count):
                next_word_idx = i + word_len * j
                word = s[next_word_idx : next_word_idx+word_len]

                if word not in word_map:
                    break
                
                see[word] = see.get(word,0) +1
                if see[word] > word_map.get(word,0):
                    break
                if j +1 ==word_count:
                    ans.append(i)

        return ans

