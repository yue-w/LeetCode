


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= n - 1
        return count

if __name__ == '__main__':
    s = Solution()
    binary = '0b00000000000000000000000000001011'
    n = int(binary,2)
    print(s.hammingWeight(n))
