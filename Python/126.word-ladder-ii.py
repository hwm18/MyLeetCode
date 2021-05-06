#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (23.51%)
# Likes:    2472
# Dislikes: 298
# Total Accepted:    226.5K
# Total Submissions: 946.9K
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
# Given two words, beginWord and endWord, and a dictionary wordList, return all
# the shortest transformation sequences from beginWord to endWord, or an empty
# list if no such sequence exists. Each sequence should be returned as a list
# of the words [beginWord, s1, s2, ..., sk].
# 
# 
# Example 1:
# 
# 
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# Explanation: There are 2 shortest transformation sequences:
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# "hit" -> "hot" -> "lot" -> "log" -> "cog"
# 
# 
# Example 2:
# 
# 
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# Output: []
# Explanation: The endWord "cog" is not in wordList, therefore there is no
# valid transformation sequence.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= beginWord.length <= 5
# endWord.length == beginWord.length
# 1 <= wordList.length <= 1000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
# 
# 
#

# @lc code=start
class Solution:
    # Solution 1: BFS + DFS 
    # 从 end 到 start 做一次 BFS，并且把距离 end 的距离都保存在 distance 中。 然后在从 start 到 end 做一次 DFS，每走一步必须确保离 end 的 distance 越来越近。
    # 与另外一个代码中提前建立 index 不同，这里是在寻找下一个变换单词的时候，再去获得对应的单词列表。一个单词最多有 L 个字符，每个字符有 25 种不同的变化（26个字母除掉这个位置上的字母），
    # 然后 check 一下在不在 dict 里就知道是不是 next word 了。
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not wordList or endWord not in wordList:
            return []
            
        wordList.append(beginWord)
        wordList.append(endWord)
        distance = {}
        
        self.bfs(endWord, distance, wordList)
        
        results = []
        self.dfs(beginWord, endWord, distance, wordList, [beginWord], results)
        
        return results

    def bfs(self, start, distance, dict):
        distance[start] = 0
        queue = deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, dict):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)
    
    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in dict:
                    words.append(next_word)
        return words
                        
    def dfs(self, curt, target, distance, dict, path, results):
        if curt == target:
            results.append(list(path))  # deep copy
            return
        
        for nextWord in self.get_next_words(curt, dict):
            if distance[nextWord] != distance[curt] - 1:
                continue

            path.append(nextWord)
            self.dfs(nextWord, target, distance, dict, path, results)
            path.pop()
        
# @lc code=end

