
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        Use sorting to simplify the problem.
        """
        digits = str(n)
        digits = [c for c in digits]
        digits.sort()
        
        ## iterate
        for i in range(33):
            two_pow = 1 << i
            two_pow = str(two_pow)
            two_pow = [c for c in two_pow]
            two_pow.sort()
            if two_pow == digits:
                return True
        
        return False