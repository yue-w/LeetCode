# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:28:36 2020

@author: wyue
"""
""""

"""
class Trie():
    def __init__(self):
        self.next = [None] * 26
        self.isword = False

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        ptr = self.trie
        for w in word:
            idx = ord(w) - ord('a')
            if not ptr.next[idx]:
                ptr.next[idx] = Trie()
            ptr = ptr.next[idx]
        ptr.isword = True

    def search(self, word: str) -> bool:
        def dfs(i, ptr):
            ## Base case of recursion
            if not ptr:
                return False
            if i == len(word):
                return ptr.isword
            if word[i] != '.':
                idx = ord(word[i]) - ord('a')
                return dfs(i+1, ptr.next[idx])
            else:
                for j in range(26):
                    if dfs(i+1, ptr.next[j]):
                        return True
                return False
        
        return dfs(0, self.trie)
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord("aa")

    print(obj.search("a.")) #return False


