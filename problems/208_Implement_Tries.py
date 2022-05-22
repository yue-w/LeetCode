# -*- coding: utf-8 -*-
class Trie:

    def __init__(self):
        self.pointers = [None] * 26
        self.is_word = None

    def insert(self, word: str) -> None:
        node = self
        for w in word:
            index = ord(w) - ord('a')
            if not node.pointers[index]:
                node.pointers[index] = Trie()
            node = node.pointers[index]
                
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self
        for w in word:
            index = ord(w) - ord('a')
            if not node.pointers[index]:
                return False
            node = node.pointers[index]
        
        return node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        node = self
        for w in prefix:
            index = ord(w) - ord('a')
            if not node.pointers[index]:
                return False
            node = node.pointers[index]
        
        return True


##Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert('app')
trie.insert('apple')
print(trie.search('app'))