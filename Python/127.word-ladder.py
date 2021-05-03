#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Hard (31.58%)
# Likes:    4952
# Dislikes: 1416
# Total Accepted:    573.8K
# Total Submissions: 1.8M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# A transformation sequence from word beginWord to word endWord using a
# dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
# such that:
# 
# 
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to
# be in wordList.
# sk == endWord
# 
# 
# Given two words, beginWord and endWord, and a dictionary wordList, return the
# number of words in the shortest transformation sequence from beginWord to
# endWord, or 0 if no such sequence exists.
# 
# 
# Example 1:
# 
# 
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot"
# -> "dog" -> cog", which is 5 words long.
# 
# 
# Example 2:
# 
# 
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no
# valid transformation sequence.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
# 
# 
#

# @lc code=start
class Solution:
    # solution 2: 不使用分层遍历的版本。使用 distance 这个 hash 来存储距离来实现记录每个节点的距离。
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0
        
        wordList.append(endWord)
        queue = collections.deque([beginWord])
        distance = {beginWord: 1}

        while queue:
            word = queue.popleft()
            if word == endWord:
                return distance[word]
            
            for nextWord in self.get_next_words(word, wordList):
                if nextWord in distance:
                    continue
                
                queue.append(nextWord)
                distance[nextWord] = distance[word] + 1
        
        return 0
    
    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                next_word = left + char + right
                if next_word in dict:
                    words.append(next_word)

        return words


    '''
    # solution 1: 使用分层遍历的BFS版本。
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0

        wordList.append(endWord)
        queue = collections.deque([beginWord])
        visited = set([beginWord])

        length = 0
        while queue:
            n = len(queue)
            length +=1
            for i in range(n):
                word = queue.popleft()
                if word == endWord:
                    return length
                
                for new_word in self.getNext(word):
                    if new_word not in wordList or new_word in visited:
                        continue

                    queue.append(new_word)
                    visited.add(new_word)
                
        return 0
    
    def getNext(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words
    '''
        
# @lc code=end

