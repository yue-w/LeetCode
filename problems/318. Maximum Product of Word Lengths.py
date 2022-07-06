from typing import List
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        #return self.method1(words)
        return self.method2(words) ## preferred method
    
    def method1(self, words):
        """
        convert each word into a vocabulary table.
        Time:O(n^2)
        Space: O(n)
        """
        def word_to_table(word):
            table = [0] * 26
            for w in word:
                table[ord(w) - ord('a')] += 1    
            return table
        
        def common_letters(tables, i, j):
            for k in range(26):
                if tables[i][k] > 0 and tables[j][k] > 0:
                    return True
            return False
        
        tables = [[] for _ in range(len(words))]
        rst = 0
        for i in range(len(words) - 1):
            if not tables[i]:
                tables[i] = word_to_table(words[i])
            for j in range(i+1, len(words)):
                if not tables[j]:
                    tables[j] = word_to_table(words[j])
                if not common_letters(tables, i, j):
                    rst = max(rst, len(words[i]) * len(words[j]))
        return rst

    
    def method2(self, words):
        """
        Similar ideas with method1 but use an int to represent the state of 
        a word. Use the first 26 bit to represent whether a character exists.
        Then if two words have the same characters, their bitwise and would be 
        larger than 0.
        Time:O(n^2)
        Space: O(n)
        """
        bits = [0] * len(words)
        for i in range(len(words)):
            v = 0
            for k in range(len(words[i])):
                ## bitwise or
                v = v| (1 << (ord(words[i][k]) - ord('a')))
            
            bits[i] = v
                
        rst = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                ## bitwise and
                if bits[i] & bits[j] != 0:
                    continue
                rst = max(rst, len(words[i]) * len(words[j]))

        return rst
    
                
                
                
 