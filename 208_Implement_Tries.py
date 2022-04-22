# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 18:05:20 2020

@author: wyue
"""

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pointers = [None]*27
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        
        node = self
        for char in word:
            index = ord(char) - 97 + 1
            if node.pointers[index] is None:
                node.pointers[index] = Trie()
            node = node.pointers[index]
        node.pointers[0] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self
        for char in word:
            index = ord(char) - 97 + 1
            node = node.pointers[index]
            if not node:
                return False
        if node.pointers[0]:
            return True
        else:
            return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self
        for char in prefix:
            index = ord(char) - 97 + 1
            node = node.pointers[index]
            if not node:
                return False
        return True



##Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert('app')
trie.insert('apple')
print(trie.search('app'))