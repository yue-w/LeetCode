

class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        ## find how many fives (and its powers) are there
        rst = 0
        i = 1
        while (5 ** i) <= n:
            k = 0
            while k * (5 ** i) <= n:
                k += 1
                if k * (5 ** i) > n:
                    break
            rst += k - 1 
            i += 1
        
        
        return rst

if __name__ == '__main__':
    s = Solution()
    n = 5
    rst = s.trailingZeroes(30)
    print(rst)