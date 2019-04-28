#
# @lc app=leetcode id=288 lang=python
#
# [288] unique-word-abbreviation
#https://www.lintcode.com/problem/unique-word-abbreviation/description
# https://leetcode.com/problems/unique-word-abbreviation/description/
#
# An abbreviation of a word follows the form . Below are some examples of word abbreviations:
# a) it                      --> it    (no abbreviation)

#      1
# b) d|o|g                   --> d1g

#               1    1  1
#      1---5----0----5--8
# c) i|nternationalizatio|n  --> i18n

#               1
#      1---5----0
# d) l|ocalizatio|n          --> l10n
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. 
# A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.
# 
# Example1
# Input:
# [ "deer", "door", "cake", "card" ]
# isUnique("dear")
# isUnique("cart")
# Output:
# false
# true
# Explanation:
# Dictionary's abbreviation is ["d2r", "d2r", "c2e", "c2d"].
# "dear" 's abbreviation is "d2r" , in dictionary.
# "cart" 's abbreviation is "c2t" , not in dictionary.
# Example2

# Input:
# [ "deer", "door", "cake", "card" ]
# isUnique("cane")
# isUnique("make")
# Output:
# false
# true
# Explanation:
# Dictionary's abbreviation is ["d2r", "d2r", "c2e", "c2d"].
# "cane" 's abbreviation is "c2e" , in dictionary.
# "make" 's abbreviation is "m2e" , not in dictionary.
# 
# 
#
class ValidWordAbbr:
    """
    @param: dictionary: a list of words
    """
    def __init__(self, dictionary):
        # do intialization if necessary
        self.map = {}
        for s in dictionary:
            abbr = self.getAbbr(s)
            if abbr not in self.map:
                self.map[abbr] = set()
            self.map[abbr].add(s)
            
    def getAbbr(self, s):
        if len(s) <=1:
            return s
        return s[0] + str(len(s[1:-1]))+s[-1]

    """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """
    def isUnique(self, word):
        # write your code here
        w = self.getAbbr(word)
        if w not in self.map:
            return True
        for item in self.map[w]:
            if word != item:
                return False
            
        return True

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param = obj.isUnique(word)





