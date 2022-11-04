from typing import List

class Trie:
    def __init__(self):
        self.voc = [None] * 26
        self.is_word = False
        
    def add(self, word):
        ptr = self
        for w in word:
            index = ord(w) - ord('a')
            if not ptr.voc[index]:
                ptr.voc[index] = Trie()
            ptr = ptr.voc[index]
        ptr.is_word = True
            
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        Trie + dfs (backtracking).
        """
        trie = Trie()
        for product in products:
            trie.add(product)
        rst = [[] for _ in range(len(searchWord))]

        ptr = trie
        run_word = []
        for i, char in enumerate(searchWord):
            curr = []
            ptr = ptr.voc[ord(char) - ord('a')]
            if not ptr:
                return rst
            run_word.append(char)
            self.dfs(curr, run_word, ptr)
            
            rst[i] = curr
        return rst
    
    def dfs(self, curr, run_word, ptr):
        ## base case:
        if len(curr) == 3:
            return
        if ptr.is_word:
            curr.append(''.join(run_word))
        
        for i in range(26):
            if ptr.voc[i]: 
                run_word.append(chr(i + ord('a')) )
                self.dfs(curr, run_word, ptr.voc[i])
                ## back tracking
                run_word.pop()
        return
                
            
            
if __name__ == '__main__':
    products = ["bags","baggage","banner","box","cloths"]
    searchWord = "bags"  
    # products = ["havana"]
    # searchWord = "tatiana"
    rst = Solution().suggestedProducts(products, searchWord)
    print(rst)        