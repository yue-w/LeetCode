"""
My implementation of the Quicksort algorithm. 
Sort an arrayof numbers in ascending order.
"""
def quick_sort(A, start=0, end=None):
	if end is None:
		end = len(A) - 1
	## Base case
	if start >= end:
		return
	pivot_index = find_pivot(start, end)
	## swap element at first and pivot_index
	A[start], A[pivot_index] = A[pivot_index], A[start]
	
	left, right = partition(A, start, end)
	## After calling partition, the A[partition_index] is at right position

	## Recursion, left part
	quick_sort(A, start,  left)
	## Recursion, right part
	quick_sort(A, right, end)



def find_pivot(left, right):
	"""
	This implement return the mid point between left and right
	"""
	return left + (right - left) // 2

def partition(A, start, end):
	"""
	Quick select (three pointers).
	Time: O(n)
	Space: O(1)
	S: Smaller, E: Equal, U: Unknown, L: larger
	S S S S E E E E E U U U U U U U L L L L L L L
			|         |           |
		   left      curr       right
	when returned from the recursion, the final state
	S S S S E E E E E E E E E E E E L L L L L L L
			|                     |
		  left                 right (curr)
	"""
	pivot = A[start]
	left = start
	curr = left
	right = end

	while curr <= right:
		if A[curr] < pivot:
			A[left], A[curr] = A[curr], A[left]
			left += 1
			curr += 1
		elif A[curr] == pivot:
			curr += 1
		else: # A[curr] > pivot
			A[right], A[curr] = A[curr], A[right]
			right -= 1

	return left - 1, right + 1

	
if __name__ == '__main__':
	A = [100,3,2,1,4,6,5,43,43, 7,8, 0]
	quick_sort(A)
	print(A)