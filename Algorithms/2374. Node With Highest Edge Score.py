
from typing import List
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        score = [0] * n
        for idx, nxt in enumerate(edges):
            score[nxt] += idx
        
        rst = 0
        maxv = -1
        for i, s in enumerate(score):
            if maxv < s:
                rst = i
                maxv = s
        
        return rst