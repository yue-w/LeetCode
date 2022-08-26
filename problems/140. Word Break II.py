from typing import List

class TrieNode:
    def __init__(self):
        self.nxt = [None] * 26
        self.is_word = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        Trie. DFS. Backtracking.
        """
        def dfs(curr, idx):
            ## base case
            if idx == n:
                rst.append(' '.join(curr))
                return True
            
            if idx in memo:
                return False
            
            node = root
            found_one = False
            for i in range(idx, n):
                if not node.nxt[ord(s[i]) - ord('a')]:
                    break
                
                node = node.nxt[ord(s[i]) - ord('a')]
                
                if node.is_word:
                    curr.append(s[idx:i+1])
                    if dfs(curr, i+1):
                        found_one = True
                    curr.pop()
            
            if not found_one:
                memo.add(idx)
                
            return found_one
            
        ## step 1: build trie.
        root = TrieNode()
        for word in wordDict:
            node = root
            for w in word:
                idx = ord(w) - ord('a')
                if not node.nxt[idx]:
                    node.nxt[idx] = TrieNode()
                node = node.nxt[idx]
            node.is_word = True  
        
        curr = []
        rst = []
        n = len(s)
        memo = set()
        dfs(curr, 0)

        return rst
if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat","cats","and","sand","dog"]
    rst = Solution().wordBreak(s, wordDict)
    print(rst)