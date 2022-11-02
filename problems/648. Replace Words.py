from typing import List

class Trie:
    def __init__(self):
        self.pointers = [None for _ in range(26)]
        self.is_end = False
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        Trie
        Simplify dictionary (when have same prefix, keep the shortest). E.g. 'a', and 'aa', keep 'a' only.
        """
        trie = self.form_trie(dictionary)
        rst = []
        words = sentence.split(' ')
        for word in words:
            curr = trie
            found = False
            for i, w in enumerate(word):
                if not curr:
                    break
                if curr.is_end:
                    rst.append(word[:i])
                    found = True
                    break
                curr = curr.pointers[ord(w) - ord('a')]
            if not found:
                rst.append(word)

        
        return ' '.join(rst)
        
    def form_trie(self, dictionary):
        """
        From words, build a trie. Remove long trie if overlap/
        """
        trie = Trie()
        for root in dictionary:
            curr = trie
            for r in root:
                if not curr.pointers[ord(r) - ord('a')]:
                    curr.pointers[ord(r) - ord('a')] = Trie()    
                curr = curr.pointers[ord(r) - ord('a')]
            curr.is_end = True

        return trie
        