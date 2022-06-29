# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:28:36 2020

@author: wyue
"""
""""
Solution 1:
"""
class Trie:
    def __init__(self):
        self.voc = {}
        self.isword = False


class WordDictionary:

    def __init__(self):
        self.trie = Trie()
        
    def addWord(self, word: str) -> None:
        ptr = self.trie
        for w in word:
            #index = ord(w) - ord('a')
            ptr = ptr.voc.setdefault(w, Trie())

        ptr.isword = True

    def search(self, word: str) -> bool:
        ptr = self.trie
        return self.dfs(ptr, word, 0)
    
    def dfs(self, ptr, word, i):
        ## base case:
        # if not ptr:
        #     return False
        if i == len(word):
            return ptr.isword
        
        ## recursion
        if word[i] != '.':
            if word[i] in ptr.voc:
                ptr = ptr.voc[word[i]]
                return self.dfs(ptr, word, i + 1)
            else:
                return False
        else:
            for w in ptr.voc:
                ptrcp = ptr.voc[w]
                if self.dfs(ptrcp, word, i + 1):
                    return True
                
            return False


"""
Solution 2: 
Same method with method 1, but use a table of length 26 instead of hashing.
This method TLE. Maybe constructing tables take too much time.
"""
## Defination of a class Trie
class Trie:
    def __init__(self):
        self.voc = [None for _ in range(26)] 
        self.isword = False
class WordDictionary:

    def __init__(self):
        self.trie = Trie()
        
    def addWord(self, word: str) -> None:
        ptr = self.trie
        for w in word:
            index = ord(w) - ord('a')
            if not ptr.voc[index]:
                ptr.voc[index] = Trie()
                ptr = ptr.voc[index]
            else:
                ptr = ptr.voc[index]

        ptr.isword = True

    def search(self, word: str) -> bool:
        ptr = self.trie
        return self.dfs(ptr, word, 0)
    
    def dfs(self, ptr, word, i):
        ## base case:
        # if not ptr:
        #     return False
        if i == len(word):
            return ptr.isword
        
        ## recursion
        if word[i] != '.':
            index = ord(word[i]) - ord('a')
            if ptr.voc[index]:
                ptr = ptr.voc[index]
                return self.dfs(ptr, word, i + 1)
            else:
                return False
        else:
            for index in range(26):
                ptrcp = ptr.voc[index]
                if not ptrcp:
                    continue
                if self.dfs(ptrcp, word, i + 1):
                    return True
                
            return False
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    print(obj.search("pad")) #return False
    print(obj.search("bad")) # return True
    print(obj.search(".ad")) #return True
    print(obj.search("b..")) #return True
    print(obj.search('t..'))

