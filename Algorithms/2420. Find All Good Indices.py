

from typing import List
from collections import deque
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        #return self.method1(nums, k)
        #return self.method2(nums, k)
        return self.method3(nums, k)# preferred method
    
    def method1(self, nums, k):
        """
        Deque.
        Forward then backward
        """
        stack_dec = deque()
        rst1 = set()
        rst2 = set()
        n = len(nums)
        for i in range(n):
            if k <= i < n - k and len(stack_dec) == k:
                rst1.add(i)
            if (not stack_dec) or nums[stack_dec[-1]] >= nums[i]:
                stack_dec.append(i)
            else:
                stack_dec = deque()
                stack_dec.append(i)

            if stack_dec and stack_dec[0] <= i - k :
                stack_dec.popleft()
        
        stack_inc = deque()
        for i in range(n - 1, -1, -1):
            if k <= i < n - k and len(stack_inc) == k and i in rst1:
                rst2.add(i)
            if (not stack_inc) or nums[stack_inc[0]] >= nums[i]:
                stack_inc.appendleft(i)
            else:
                stack_inc = deque()
                stack_inc.append(i)

            if stack_inc and stack_inc[-1] >= i + k :
                stack_inc.pop()
        rst = list(rst2)
        rst.sort()
        return rst
    
    def method2(self, nums, k):
        """
        Same idea with method1 (use deque), but one pass.
        """
        dq_dec = deque()
        dq_inc = deque()
        n = len(nums)
        # Initialize the k numbers before
        for i in range(k):
            ## decrease
            if dq_dec and nums[i] <= nums[dq_dec[-1]]:
                dq_dec.append(i)
            else:
                dq_dec = deque([i])
                
        # initialize the k numbers after
        for i in range(k + 1, min(n, 2 * k + 1)):
            ## increase
            if dq_inc and nums[i] >= nums[dq_inc[-1]]:
                dq_inc.append(i)
            else:
                dq_inc = deque([i])
        # print(dq_dec)
        # print(dq_inc)
        rst = []
        for i in range(k, n - k):
            if (len(dq_dec) == k) and (len(dq_inc) == k):
                rst.append(i)
            
            if dq_dec and nums[dq_dec[-1]] >= nums[i]:
                dq_dec.append(i)
            else:
                dq_dec = deque([i])
            if dq_inc and (i + k + 1) < n and nums[dq_inc[-1]] <= nums[i + k + 1]:
                dq_inc.append(i + k + 1)
            else:
                dq_inc = deque([i + k + 1])
            
            if dq_dec and dq_dec[0] <= i - k:
                dq_dec.popleft()
            if dq_inc and dq_inc[0] <= i + 1:
                dq_inc.popleft()
        
        return rst
    
    def method3(self, nums, k):
        n = len(nums)
        dec = [1] * n
        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                dec[i] = dec[i - 1] + 1
        inc = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                inc[i] = inc[i + 1] + 1
        
        rst = []
        for i in range(k, n - k):
            if dec[i - 1] >= k and inc[i + 1] >= k:
                rst.append(i)
        return rst

        
if __name__ == '__main__':
    nums = [1,2,1,2,1,2,3,4]
    k = 1
    rst = Solution().goodIndices(nums,k)
    print(rst)

        