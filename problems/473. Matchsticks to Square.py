from typing import List
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        Backtracking with memo
        Reference: https://youtu.be/hUe0cUKV-YY
        """
        total = sum(matchsticks)
        if total  % 4 != 0:
            return False
        side = int(total / 4)
        matchsticks.sort(reverse=True)
        sides = [0] * 4
        
        memo = set()
        
        def dfs(i):
            ## base case
            if i == len(matchsticks):
                return True
            if tuple(sides) in memo:
                return False
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= side:
                    sides[j] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    ## bracktracking
                    sides[j] -= matchsticks[i]
            memo.add(tuple(sides))
            return False

            
        return dfs(0)
if __name__ == '__main__':
    #matchsticks = [5,5,5,5,4,4,4,4,3,3,3,3]
    #matchsticks = [2,2,2,2,2,6]
    #matchsticks = [1,1,2,2,2]
    #matchsticks = [3,3,3,3,4]
    matchsticks = [3,1,3,3,10,7,10,3,6,9,10,3,7,6,7]
    rst = Solution().makesquare(matchsticks)
    print(rst)
    """

    [1,1,2,2,2]
    [5,5,5,5,16,4,4,4,4,4,3,3,3,3,4]
    [12,12,12,16,20,24,28,32,36,40,44,48,52,56,60]
    [3,1,3,3,10,7,10,3,6,9,10,3,7,6,7]    
    [100,100,100,100,100,100,100,100,4,100,2,2,100,100,100]
    """