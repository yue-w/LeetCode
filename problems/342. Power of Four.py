

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return self.method2(n)
    
    def method1(self, n):
        while n >= 4:
            n /= 4
        return n == 1 
    
    def method2(self, n):
        """
        follow up. No loop
        Reference: https://leetcode.com/problems/power-of-four/discuss/80461/Python-one-line-solution-with-explanations
        Power of 4 should be one of the following numbers (in binary)
        1
        100
        10000
        1000000
        100000000
        10000000000
        1000000000000
        100000000000000
        10000000000000000
        1000000000000000000
        100000000000000000000
        10000000000000000000000
        1000000000000000000000000
        100000000000000000000000000
        10000000000000000000000000000
        1000000000000000000000000000000
        OR them into one mask is 1010101010101010101010101010101
        """
        return (n != 0) and (n & (n - 1) == 0) and (n == (n & int('0b1010101010101010101010101010101', 2)))
        