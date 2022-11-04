

from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Reference: https://youtu.be/Kwo2jkHOyPY
        Time: n(log(logn))
        Space: O(n)
        """
        if n <= 2:
            return 0

        ## table stores whether the number is a prime
        ## consider 1, 2, ..., n - 1
        ## add 0 into the array so that we have 1 index.
        table = [1] * n
        table[0] = 0
        table[1] = 0

        i = 2
        while i <= sqrt(n):
            if table[i] == 0:
                i += 1
                continue
            j = i * i
            while j < n:
                table[j] = 0
                j += i
            i += 1

        return sum(table)


if __name__ == '__main__':
    s = Solution()
    n = 999983
    rst = s.countPrimes(n)
    print(rst)   
                    
"""
Tricks:
1. Prime's multiples are not prime
2. if n % k == 0, n is not prime. 
3. we can only consider between 0 to sqrt(n)
"""
                    
        