

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        val = self.recursion(x, abs(n))
        if n > 0:
            return val
        else:
            return 1 / val
        
    def recursion(self, x, power):
        ## base case
        if power == 0:
            return 1
        if power == 1:
            return x
        power_div = power // 2
        v = self.recursion(x, power_div)
        if power % 2:
            return v * v * x
        else:
            return v * v
"""
Divide and conquer
"""
if __name__ == '__main__':
    s = Solution()
    x = 2
    n = 10
    rst = s.myPow(2, n)
    print(rst)   