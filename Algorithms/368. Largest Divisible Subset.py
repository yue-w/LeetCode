from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        #return self.method1(nums)
        return self.method2(nums)
        
    def method1(self, nums):
        """
        DP: basic II.
        Time: O(n^2)
        Space: O(n^2)
        sort.
        count[i]: the number of the subset that include nums[i]
        rst[i]: the subset that include nums[i]
        """
        nums.sort()
        N = len(nums)
        count = [1] * N
        rst = [[nums[i]] for i in range(N)]

        for i in range(1, N):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if count[j] + 1 > count[i]:
                        count[i] = count[j] + 1
                        rst[i] = rst[j][:]
                        rst[i].append(nums[i])
        maxcount = 0            
        index = None
        for i in range(N):
            if count[i] > maxcount:
                maxcount = count[i]
                index = i
        return rst[index]
    
    def method2(self, nums):
        """
        preferred method.
        Same with method 1, but reconstruct result instead of storing rst at every state.
        Time: O(n^2)
        Space: O(n)
        dp[i]: number of largest divisible subset ending with nums[i]
        """
        nums.sort()
        N = len(nums)
        dp = [1] * N
        
        ## save the index of the previouse number that can divid nums[i] 
        prev = [-1] * N

        for i in range(1, N):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
     
        idx = 0
        maxcount = 0
        for i in range(N):
            if dp[i] > maxcount:
                maxcount = dp[i]
                idx = i
                
        rst = []
        while idx != -1:
            rst.append(nums[idx])
            idx = prev[idx]
            
        return rst

                    
if __name__ == '__main__':
    s = Solution()
    nums = [3,4,16,8]
    rst = s.largestDivisibleSubset(nums)
    print(rst)