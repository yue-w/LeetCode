
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
        
    def exist(self, word, start, end):
        """
        whether word[start:end] exist in the trie. include start, exclude end
        pass word and indexes to avoid coping strings
        """
        node = self
        #for w in word:
        while start < end:
            index = ord(word[start]) - ord('a')
            if not node.pointers[index]:
                return False
            node = node.pointers[index]
            start += 1
            
        return node.is_word
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #### Method 1
        # memo = {}
        # return self.dp_recursion(s, wordDict, memo)
        
        #### Method 2
        #return self.use_trie(s, wordDict)

        #### Method 3. This is the preferred method. Similar to method 2
        #### but removed some redundant stuff.
        return self.use_trie2(s, wordDict) ## This is the preferred method
    
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
        
        ## memo[i] == 1 means s[i:] has failed
        memo = [0] * len(s)
        return self.recursion_trie(s, 0, memo)
            
    def recursion_trie(self, s, i, memo):
        ## Base case
        if i == len(s):
            return True
        if memo[i] == 1:
            return False
        
        for k in range(1, len(s) - i + 1):
            if self.trie.exist(s, i, i + k) and self.recursion_trie(s, i + k, memo):
                return True

        memo[i] = 1
        return False
    
    def use_trie2(self, s, wordDict):
        """
        This is the preferred method
        Use trie but do not call the exist function of the Trie class,
        move the trie pointer instead
        """
        self.trie = Trie()
        for word in wordDict:
            self.trie.add(word)
        
        ## memo[i] == 1 means s[i:] has failed
        memo = [0] * len(s)

        return self.recursion_trie2(s, 0, memo)
    
    def recursion_trie2(self, s, curr, memo):
        ## Base case
        if curr == len(s):
            return True
        ## memo[i] == 1 means s[i:] has failed
        if memo[curr] == 1:
            return False
        
        trie_node = self.trie
        for i in range(curr, len(s)):
            trie_node = trie_node.pointers[ord(s[i]) - ord('a')]
            if trie_node:
                if trie_node.is_word and self.recursion_trie2(s, i + 1, memo):
                    return True
            else:
                break
        memo[curr] = 1
        return False

if __name__ == '__main__':
    s = Solution()
    string = "applepenapple" #"leetcode"  # "applepenapple"
    wordDict = ["apple","pen"] #["leet","code"] # ["apple","pen"]


    rst = s.wordBreak(string, wordDict)
    print(rst)