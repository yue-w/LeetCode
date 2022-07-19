from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:       
        """
        Time: O(nlogC)
        Space: O(1)
        """ 
        def can_finish(k):
            """
            Return whether can finish in h hours if eat k bananas / h
            """
            count = 0
            remain = 0
            i = 0
            while i < len(piles):                
                count += math.ceil(piles[i]/k)
                i += 1
                if count > h:
                    return False
            return True
              
        
        left = 1
        right = max(piles)
        
        while left < right:
            mid = left + (right - left) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
            
        return left