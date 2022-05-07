from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {nums1[i]:i  for i in range(len(nums1))}
        rst = [-1] * len(nums1)

        monotonic_stack = []
        
        for num2 in nums2:
            while monotonic_stack and monotonic_stack[-1] < num2:
                val = monotonic_stack.pop()
                idx = dic[val]
                rst[idx] = num2 
            if num2 in dic:
                monotonic_stack.append(num2)

            
        return rst

if __name__ == '__main__':
    s = Solution()
    nums1 = [4,1,2] 
    nums2 = [1,2,3,4]
    print(s.nextGreaterElement(nums1, nums2))

        