import math

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def permutation(m, n):
            rst = 1
            for i in range(n):
                rst *= m - i
            return rst
        
        ## 0 should be considered seperatly (0 is the leading 0 of 1-digit number)
        rst = 1
        for digit in range(1, n+1):
            ## method 1: write a permutation function
            # rst += permutation(10, digit) - permutation(9, digit-1)
            ## method 2: call math.perm()
            rst += math.perm(10, digit) - math.perm(9, digit - 1)
        
        return rst