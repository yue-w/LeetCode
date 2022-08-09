
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
        DP
        """
        if stones[1] - stones[0] != 1:
            return False
        
        n = len(stones)
        
        def dfs(stone, steps):
            ## base case
            if stone == stones[-1]:
                return True

            if (stone, steps) in memo:
                return False
            
            ## steps - 1    
            if steps - 1 > 0 and stone + steps - 1 in dis and dfs(stone + steps - 1, steps - 1):
                return True
            
            ## steps 
            if stone + steps in dis and dfs(stone + steps, steps):
                return True
            
            ## steps + 1
            if stone + steps + 1 in dis and dfs(stone + steps + 1, steps + 1):
                return True
            
            memo.add((stone, steps))
            return False
                    
        dis = set(stones)
        memo = set()
        return dfs(1, 1)


if __name__ == '__main__':
    stones =  [0,1,3,5,6,8,12,17]
    rst = Solution().canCross(stones)
    print(rst)