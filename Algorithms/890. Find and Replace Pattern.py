from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """
        Time: O(m*n)
        """
        rst = []
        m = len(pattern)
        for word in words:
            if len(word) != m:
                continue
            dic = {}
            dic2 = {}
            match = True
            for w, p in zip(word, pattern):
                if (p in dic and dic[p] != w) or (w in dic2 and dic2[w] != p):
                    match = False
                    break
                dic[p] = w
                dic2[w] = p
            if match:
                rst.append(word)

        
        return rst