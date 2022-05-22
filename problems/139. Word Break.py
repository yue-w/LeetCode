
from typing import List

class Trie:
    def __init__(self):
        self.pointers = [None] * 26
        self.is_word = None
        
    def add(self, word):
        node = self
        for w in word:
            index = ord(w) - ord('a')
            if not node.pointers[index]:
                node.pointers[index] = Trie()
            node = node.pointers[index]
        node.is_word = True
        
    def exist(self, word):
        node = self
        for w in word:
            index = ord(w) - ord('a')
            if not node.pointers[index]:
                return False
            node = node.pointers[index]
            
        return node.is_word
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # memo = {}
        # return self.dp_recursion(s, wordDict, memo)
        
        return self.use_trie(s, wordDict)
    
    def dp_recursion(self, remain, wordDict, memo):
        ## Base case
        if not remain:
            return True
        if remain in memo:
            return memo[remain]
        
        for word in wordDict:
            if word == remain[:len(word)]:
                if self.dp_recursion(remain[len(word):], wordDict, memo):
                    memo[remain] = True
                    return True
        memo[remain] = False    
        return False
    
    def use_trie(self, s, wordDict):
        self.trie = Trie()
        for word in wordDict:
            self.trie.add(word)
        memo = [0] * len(s)
        return self.recursion_trie(s, 0, memo)
            
    def recursion_trie(self, s, i, memo):
        ## Base case
        if i == len(s):
            return True
        if memo[i] == 1:
            return False
        
        for k in range(1, len(s) - i + 1):
            if self.trie.exist(s[i: i + k]):
                remain = self.recursion_trie(s, i + k, memo)
                if remain:
                    return True
        memo[i] = 1
        return False

if __name__ == '__main__':
    s = Solution()
    string = "applepenapple" #"leetcode"  # "applepenapple"
    wordDict = ["apple","pen"] #["leet","code"] # ["apple","pen"]


    rst = s.wordBreak(string, wordDict)
    print(rst)