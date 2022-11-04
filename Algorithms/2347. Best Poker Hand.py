from typing import List
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        from collections import Counter
        if len(set(suits)) == 1:
            return "Flush"
        
        counter = Counter(ranks)
        count = counter.most_common(1)[0][1]
        if count >= 3:
            return "Three of a Kind"
        if count == 2:
            return "Pair"
        return "High Card"
        
