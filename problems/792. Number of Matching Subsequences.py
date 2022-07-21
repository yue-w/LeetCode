from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        def subseq(s, word):
            """
            Retirm whether whether word is a substring of s
            """
            if len(word) > len(s):
                return False
            table = [0] * 26
            
            for w in word:
                table[ord(w) - ord('a')] += 1
            
            table2 = [0] * 26
            for i in range(len(s)):
                table2[ord(s[i]) - ord('a')] += 1
                if i >= len(word) - 1:
                    if table == table2:
                        return True
                    table2[ord(s[i - len(word) + 1]) - ord('a')] -= 1
                    
            return False
        
        def subseq2(s, word):
            if len(word) > len(s):
                return False
            j = 0
            for i in range(len(word)):
                if j >= len(s):
                    return False
                if s[j] == word[i]:
                    j += 1
                else:
                    while j <= len(s):
                        if j == len(s):
                            return False
                        while word[i] != s[j]:
                            j += 1  

            return True
            
        counter = Counter(words)
        
        rst = 0
        for word in counter.keys():
            if subseq2(s, word):
                rst += counter[word]
         
        return rst
                
        

            