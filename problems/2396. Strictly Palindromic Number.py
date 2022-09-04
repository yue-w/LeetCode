

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def to_base_b(n, b):
            digits = []
            while n:
                v = n % b
                digits.append(v)
                n = n // b
            return digits
        
        def is_par(digits):
            return digits == digits[::-1]
        
        for b in range(n - 2, 1, -1):
            digits = to_base_b(n, b)
            if not is_par(digits):
                return False
        
        return True
            