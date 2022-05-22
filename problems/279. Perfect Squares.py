

class Solution:
    def numSquares(self, n: int) -> int:

        return self.tabular(n)
        
    def tabular(self, n):
        array = [n] * (n + 1)
        
        ## Base case
        array[0] = 0
        
        for i in range(1, n + 1):
            j = 0
            while j * j <= i:
                array[i] = min(array[i], 1 + array[i - j * j])
                j += 1
        
        return array[n]

    def recursion(self, ):
        pass
        
            
        
if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(12))