
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        repetative nums?
        Two pointers
        Quick sort
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i - 1] >= nums[i]:
                i -= 1
            else:
                break
        if i > 0:
            ## find j
            i -= 1
            j = len(nums) - 1
            while j > i:
                if nums[j] > nums[i]:
                    break
                else:
                    j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            ## use quick sort to sort nums[i + 1:]
            #self.quick_sort(nums, i+1, len(nums) - 1)
            cp = nums[i + 1:]
            cp.sort()
            nums[i + 1:] = cp
        else:
            #self.quick_sort(nums, 0, len(nums) - 1)
            nums.sort()
        
    def quick_sort(self, A, left=0, right=None):
        if not right:
            right = len(A) - 1
        ## Base case
        if left >= right:
            return
        pivot_index = self.find_pivot(left, right)
        ## swap element at first and pivot_index
        A[left], A[pivot_index] = A[pivot_index], A[left]

        partition_index = self.partition(A, left, right)
        ## After calling partition, the A[partition_index] is at right position

        ## Recursion, left part
        self.quick_sort(A, left, partition_index - 1)
        ## Recursion, right part
        self.quick_sort(A, partition_index + 1, right)



    def find_pivot(self, left, right):
        """
        This implement return the mid point between left and right
        """
        return left + (right - left) // 2

    def partition(self, A, left, right):
        p = A[left]
        i = left + 1
        for j in range(left + 1, right + 1):
            if A[j] < p:
                A[i], A[j] = A[j], A[i]
                i += 1
        ## swap A[left] and A[i - 1]
        A[left], A[i - 1] = A[i - 1], A[left]
        return i - 1

            
if __name__ == '__main__':
    s = Solution()
    nums = [3,2,1]
    s.nextPermutation(nums)
    print(nums)
        
        
        