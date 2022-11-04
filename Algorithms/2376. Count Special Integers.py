

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        self.rst = 0
        nn = str(n)
        self.used = [0] * 10
        
        ## for numbers have less digits
        for i in range(1, len(nn)):
            ## how many ways to select i numbers from 0~9 (first digit cannot be 0)
            ## this equals to number of ways to select i numbers from 0~9 minus the number of ways
            ## to select i-1 numbers when the first digit being fixed as 0.
            self.rst += self.permutation(10, i) - self.permutation(9, i-1)
            
        ## for the numbers have the same digits
        self.dfs(nn, 0)
        return self.rst
    def permutation(self, a, b):
        """
        return the ways of arranging b differnet numbers out of a different numbers (order matters)
        """
        rst = 1
        for i in range(b):
            rst *= a - i

        return rst
    
    def dfs(self, nn, idx):
        ## base case
        if idx == len(nn):
            self.rst += 1
            return

        for d in range(0, 10):
            ## no leading 0
            if idx == 0 and d == 0:
                continue
            if self.used[d] == 1:
                continue
            if d < int(nn[idx]):
                self.rst += self.permutation(10 - idx - 1, len(nn) - idx - 1)
            elif d == int(nn[idx]):
                self.used[d] = 1
                self.dfs(nn, idx + 1)
                self.used[d] = 0


if __name__ == '__main__':
    n = 135
    rst = Solution().countSpecialNumbers(n)
    print(f'Result: {rst}')
    print(f'Expected: {110}')