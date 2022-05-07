
from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_cap = sum(weights) 

        ## do binary search 
        left = 0
        right = max_cap

        while left < right:
            mid = left + (right - left) // 2
            if self.can_shift(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        return left
        
        
        
    def can_shift(self, weights: List[int], day: int, cap: int) -> bool:
        """
        Return wheter it is possible to shift the weights (weights) in the given days 
        (day) with given capacity (cap)
        """
        d = 0
        index = len(weights) - 1
        while d < day:
            d += 1
            remain_cap = cap
            ## a new day, full capacity, if full capacity cannot ship, return false.
            if weights[index] > remain_cap:
                return False
            while remain_cap > 0:
                if index < 0:
                    return True 
                ## ship as much as possible
                if remain_cap - weights[index] >= 0:
                    remain_cap -= weights[index]
                    index -= 1
                else:
                    break
                
            if index < 0:
                return True


        return False

    

if __name__ == '__main__':

    s = Solution()
    weights = [5,5,5,5,5,5,5,5,5,5]
    days = 8
    print(s.shipWithinDays(weights, days))