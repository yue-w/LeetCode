
def quick_sort(A, left=0, right=None):
	if not right:
		right = len(A) - 1
	## Base case
	if left >= right:
		return
	pivot_index = find_pivot(left, right)
	## swap element at first and pivot_index
	A[left], A[pivot_index] = A[pivot_index], A[left]
	
	partition_index = partition(A, left, right)
	## After calling partition, the A[partition_index] is at right position

	## Recursion, left part
	quick_sort(A, left, partition_index - 1)
	## Recursion, right part
	quick_sort(A, partition_index + 1, right)



def find_pivot(left, right):
	"""
	This implement return the mid point between left and right
	"""
	return left + (right - left) // 2

def partition(A, left, right):
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
	A = [3, 1, 2, 4]
	quick_sort(A)
	print(A)