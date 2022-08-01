


class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        the number of fives contributed by 5**i is i.
        in each iteration, we count one of the 5s.
        For example for 125 = 5**3 contributes three 5s, the first 5 is counted
        in the loop of 5**1, the second 5 is counted in the loop of 5**2, and 
        the third 5 is counted in the loop of 5**3. 
        """
        rst = 0
        i = 1
        while (5 ** i) <= n:
            k = 1
            while k * (5 ** i) <= n:
                k += 1

            rst += k - 1 
            i += 1
        
        
        return rst

if __name__ == '__main__':
    s = Solution()
    n = 126
    rst = s.trailingZeroes(n)
    print(rst)