from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        return self.method1(matchsticks)
        #return self.method2(matchsticks) # preferred method

    def method1(self, matchsticks):
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

    def method2(self, matchsticks):
        
        def dfs(count, curlen, index):
            if count == 4:
                return True
            if curlen > edgeL:
                return False
            if curlen == edgeL:
                # if current length is edgeL, then start searching from the start
                return dfs(count+1, 0, 0)
            prev = -1
            for i in range(index, len(matchsticks)):
                if visited[i]:
                    continue
                if matchsticks[i] == prev:
                    continue
                prev = matchsticks[i]
                visited[i] = 1
                if dfs(count, curlen+matchsticks[i], i+1):
                    return True
                # backtracking
                visited[i] = 0
            return False

            
        total = sum(matchsticks)
        if total % 4:
            return False
        edgeL = total / 4
        visited = [0] * len(matchsticks)
        matchsticks.sort(reverse=True)
        return dfs(0, 0, 0)

if __name__ == '__main__':
    #matchsticks = [5,5,5,5,4,4,4,4,3,3,3,3]
    #matchsticks = [2,2,2,2,2,6]
    matchsticks = [1,1,2,2,2]
    #matchsticks = [3,3,3,3,4]
    #matchsticks = [3,1,3,3,10,7,10,3,6,9,10,3,7,6,7]
    rst = Solution().makesquare(matchsticks)
    print(rst)
    """

    [1,1,2,2,2]
    [5,5,5,5,16,4,4,4,4,4,3,3,3,3,4]
    [12,12,12,16,20,24,28,32,36,40,44,48,52,56,60]
    [3,1,3,3,10,7,10,3,6,9,10,3,7,6,7]    
    [100,100,100,100,100,100,100,100,4,100,2,2,100,100,100]
    """