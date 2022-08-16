
from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Two pointers
        Time: O(n1 * n2)
        """
        rst = []
        counter = Counter(words)
        lenword = len(words[0])
        for i in range(len(s)):
            if i + lenword * len(words) -1 >= len(s):
                break
                
            counter = Counter(words)
            need = len(words)
            j = i
            while counter[s[j:j+lenword]] > 0:
                counter[s[j:j+lenword]] -= 1
                j += lenword
                need -= 1
                if need == 0:
                    rst.append(i)
                    break
                
        return rst