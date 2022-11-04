from typing import List
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()

        dq = deque(range(len(deck)))
        
        rst = [0] * len(deck)
        
        ## simulate the process.
        for d in deck:
            rst[dq.popleft()] = d
            if dq:
                node = dq.popleft()
                dq.append(node)
        return rst

