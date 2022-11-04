from typing import List
from collections import defaultdict
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dic = defaultdict(list)
        idx0 = ord('a')
        for i, c in enumerate(s):
            idx = ord(c) - idx0
            dic[idx].append(i)
        
        for i, d in enumerate(distance):
            if not i in dic:
                continue
            if dic[i][1] - dic[i][0] - 1 != d:
                return False
            
        return True