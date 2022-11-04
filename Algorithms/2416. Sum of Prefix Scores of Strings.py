from typing import List

class TrieNode:
    def __init__(self):
        self.nodes = [None] * 26
        self.count = 0
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        """
        Trie
        """
        # build trie
        root = TrieNode()
        for word in words:
            node = root
            for w in word:
                idx = ord(w) - ord('a')
                if not node.nodes[idx]:
                    node.nodes[idx] = TrieNode()
                node = node.nodes[idx]
                node.count += 1
        
        rst = [0] * len(words)
        for i, word in enumerate(words):
            curr = 0
            node = root
            for w in word:
                idx = ord(w) - ord('a')
                if node.nodes[idx]:
                    node = node.nodes[idx]
                    curr += node.count
                else:
                    break
            rst[i] = curr
        
        return rst