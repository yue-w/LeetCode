

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        self.count = 0
        nn = str(n)
        self.used = [0] * 10
        
        ## for numbers have less digits
        for i in range(1, len(nn)):
            ## how many ways to select i numbers from 0~9 (first digit cannot be 0)
            ## this equals to number of ways to select i numbers from 0~9 minus the number of ways
            ## to select i-1 numbers when the first digit being fixed as 0.
            self.count += self.permutation(10, i) - self.permutation(9, i-1)
            
        ## for the numbers have the same number of digits
        self.dfs(nn, 0)
        return n - self.count
    def permutation(self, a, b):
        """
        return the ways of arranging b differnet numbers out of a different numbers (order matters)
        """
        count = 1
        for i in range(b):
            count *= a - i

        return count
    
    def dfs(self, nn, idx):
        ## base case
        if idx == len(nn):
            self.count += 1
            return

        for d in range(0, 10):
            ## no leading 0
            if idx == 0 and d == 0:
                continue
            if self.used[d] == 1:
                continue
            if d < int(nn[idx]):
                self.count += self.permutation(10 - idx - 1, len(nn) - idx - 1)
            elif d == int(nn[idx]):
                self.used[d] = 1
                self.dfs(nn, idx + 1)
                self.used[d] = 0