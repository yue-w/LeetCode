

class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        return self.recursion(1, n, memo)
            
    def recursion(self, left, right, memo):       
        ## Base case
        if left >= right:
            return 1
  
        if right - left in memo:
            return memo[right - left]
        curr = 0
        for i in range(left, right + 1):
            ## left part
            leftv = self.recursion(left, i - 1, memo)
            
            ## right part
            rightv = self.recursion(i+1, right, memo)
            curr += leftv * rightv
        memo[right - left] = curr
        return curr
        
if __name__ == '__main__':
    s = Solution()
    n = 3
    print(s.numTrees(n))