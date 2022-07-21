
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == - 2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        
        dd = abs(dividend)
        dr = abs(divisor)
        
        rst = 0

        for i in range(31, -1, -1):
            if (dr << i) <= dd:
                dd -= dr << i
                rst += 1 << i
                
        if (dividend > 0) == (divisor > 0):
            return rst
        else:
            return -rst
                