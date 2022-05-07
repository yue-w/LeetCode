


class Solution:
    def hammingWeight(self, n: int) -> int:
        rst = 0
        while n:
            if n % 2:
                rst += 1
            n = n >> 1

        return rst

if __name__ == '__main__':
    s = Solution()
    binary = '0b00000000000000000000000000001011'
    n = int(binary,2)
    print(s.hammingWeight(n))
