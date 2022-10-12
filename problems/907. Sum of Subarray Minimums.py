from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #return self.method1(arr) ## TLE
        return self.method2(arr) ## preferred method
    
    def method1(self, arr):
        """
        Brute force. TLE.
        Time: O(n^2)
        Space: O(1)
        """
        rst = 0
        for i in range(len(arr)):
            minv = float('inf')
            for j in range(i, len(arr)):
                minv = min(minv, arr[j])
                rst += minv
        
        M = int(1e9 + 7)
        return rst % M

    def method2(self, arr):
        """
        Monotonic increasing stack
        """
        rst = 0

        ## When an interval covers multiple elements of the same value, there
        ## will be duplicate. To avoid the duplicate, we only use the first
        ## smallest element. So after finding the left bound, we find left_smaller or equal.
        ## but after finding the right bound, we find the right_smaller. 
        ## left_smaller[i]: the index of the left most number that is smaller or equal than arr[i]

        ## right_smaller[i]: the index of the right most number that is smaller than arr[i]
        right_smaller = [-1] * len(arr) ## -1 is the flag value
        stack = []
        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                index = stack.pop()
                right_smaller[index] = i
            stack.append(i)
        
        left_smaller = [-1] * len(arr) ## -1 is the flag value
        stack = []
        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                index = stack.pop()
                left_smaller[index] = i
            stack.append(i)
        
        rst = 0
        for i in range(len(arr)):
            right = right_smaller[i]
            if right == -1:
                right = len(arr) - 1
            else:
                right = right - 1
            left = left_smaller[i]
            if left == -1:
                left = 0
            else:
                left = left + 1
            rst += ( (right - i + 1) * (i - left + 1)) * arr[i]

              
        M = int(1e9 + 7)
        return rst % M

if __name__ == '__main__':
    arr = [3,1,2,4]
    rst = Solution().sumSubarrayMins(arr)
    print(rst)