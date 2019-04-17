#
# @lc app=leetcode id=100 lang=python
#
#[ 408] Valid Word Abbreviation 
#
# https://www.lintcode.com/problem/valid-word-abbreviation/description
#
# algorithms
#  Easy   (29.33 %)
#
# Given a non-empty string word and an abbreviation abbr, return whether the string matches with the given abbreviation.
# A string such as "word" contains only the following valid abbreviations:

# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Notice that only the above abbreviations are valid abbreviations of the string word. Any other string is not a valid abbreviation of word.

# Have you met this question in a real interview?  
# Example 1:

# Input : s = "internationalization", abbr = "i12iz4n"
# Output : true
# Example 2:

# Input : s = "apple", abbr = "a2e"
# Output : false

# Difficulty Easy
# Total Accepted 3730
# Total Submitted 12547
# 
# 
# Your submission beats 100.00% Submissions!
class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    # Input : s = "internationalization", abbr = "i12iz4n"
    # Output : true
    def validWordAbbreviation(self, word, abbr):
        # write your code here
        if not word or not abbr:
            return False
        
        i, j = 0, 0
        while(i<len(word) and j < len(abbr)):
            # notice that 0 cannot be included
            if abbr[j]>'0' and abbr[j]<='9':  
                num = 0
                while(j < len(abbr) and abbr[j].isdigit() ):
                    num = num * 10 + int(abbr[j])
                    j += 1
                
                i += num
                if i > len(word):
                    return False
            elif word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                return False
                
        return i == len(word) and j == len(abbr)


        

