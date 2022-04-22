# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:28:36 2020

@author: wyue
"""

#### Method 1: dictionary
#class WordDictionary:
#     def __init__(self):
#         self.d = defaultdict(set)
        

#     def addWord(self, word):
#         self.d[len(word)].add(word)
        

#     def search(self, word):
#         m = len(word)
#         for dict_word in self.d[m]:
#             i = 0
#             while i < m and (dict_word[i] == word[i] or word[i] == '.'):
#                 i += 1
#             if i == m:
#                 return True
#         return False
                
#### Method 2: Trie:
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        """
        node = self.trie
        
        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True

        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any letter.
        """
        def search_in_node(word, node):
            for i, ch in enumerate(word):
                if not ch in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == '.':
                        for x in node:
                            if x != '$' and search_in_node(word[i + 1:], node[x]):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]
            return '$' in node
            
        return search_in_node(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
