from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        table = [[0 for _ in range(N)] for _ in range(N)]
        gain = self.recursion(piles, 0, len(piles) - 1, table)
        return gain > sum(piles) - gain
    
    def recursion(self, piles, i, j, table):
        ## Base case
        if i == j:
            return piles[i]
        if table[i][j] != 0:
            return table[i][j]

        
        left = piles[i] + sum(piles[i+1: j + 1]) - self.recursion(piles, i+1, j, table)
        right = piles[j] + sum(piles[i:j]) - self.recursion(piles, i, j-1, table)
        rst = max(left, right)
        table[i][j] = rst
        return rst
        

if __name__ == '__main__':
    s = Solution()
    piles = [5,3,4,5]


    print(s.stoneGame(piles))