
from typing import List
import math

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        
        #self.rst = 1
        M = int(1e9+7)
        return (self.dfs(nums) % M) - 1
     
        
    def dfs(self, array):
        if len(array) <= 1:
            return 1
        v = array[0]
        left = [array[a] for a in range(1, len(array)) if array[a] < v]
        right = [array[a] for a in range(1, len(array)) if array[a] > v]
        
        leftc = self.dfs(left)
        rightc = self.dfs(right)
        
        return leftc * rightc * math.comb(len(array)-1, len(left))
        

        