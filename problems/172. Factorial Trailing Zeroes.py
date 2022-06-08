


class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        ## find how many fives are there
        rst = 0
        i = 1
        while (5 ** i) <= n:
            k = 0
            while k * (5 ** i) <= n:
                k += 1

            rst += k - 1 
            i += 1
        
        
        return rst

if __name__ == '__main__':
    s = Solution()
    n = 5
    rst = s.trailingZeroes(n)
    print(rst)