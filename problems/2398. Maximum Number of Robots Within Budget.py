from typing import List
from collections import deque

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        left = 0
        right = n
        while left < right:
            mid = left + (right - left + 1) // 2
            if self.in_budget(mid, chargeTimes, runningCosts, budget):
                left = mid
            else:
                right = mid - 1
        return left
    
    def in_budget(self, k, chargeTimes, runningCosts, budget):
        n = len(chargeTimes)
        sumv = 0
        dq = deque()
        for i in range(n):
            sumv += runningCosts[i]
            while dq and chargeTimes[dq[-1]] <= chargeTimes[i]:
                dq.pop()
            dq.append(i)
            
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            if i - k + 1 >= 0:
                if chargeTimes[dq[0]] + k * sumv <= budget:
                    return True
                sumv -= runningCosts[i - k + 1]
            
        return False

if __name__ == '__main__':
    chargeTimes = [3,6,1,3,4]
    runningCosts = [2,1,3,4,5]
    budget = 25
    rst = Solution().maximumRobots(chargeTimes, runningCosts, budget)
    print(rst)