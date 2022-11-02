
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        from collections import Counter
        rst = []
        ct2 = {}
        for word2 in words2:
            ct2p = Counter(word2)
            for k, v in ct2p.items():
                ct2[k] = max(v, ct2.get(k, 0))
        
        for word1 in words1:
            ct1 = Counter(word1)
            all_sub = True
            for k2, v2 in ct2.items():
                if v2 > ct1[k2]:
                    all_sub = False
                    break
            if all_sub:
                rst.append(word1)
        return rst
        
#         rst = []
#         table2 = [[0 for _ in range(26)] for _ in range(len(words2))]
#         for i, word2 in enumerate(words2):
#             for w in word2:
#                 table2[i][ord(w) - ord('a')] += 1
        
#         for word1 in words1:
#             table1 = [0] * 26
#             for w in word1:
#                 table1[ord(w) - ord('a')] += 1
#             all_sub = True
#             for i in range(len(words2)):
                
#                     break
#             if all_sub:
#                 rst.append(word1)
#         return rst