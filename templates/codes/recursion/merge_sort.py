"""
Implement merge sort.
Space complexity O(n).
"""

class MergeSort:
	"""
	merge sort.
	"""
	def merge_sort(self, numbers):
		left = 0
		right = len(numbers) - 1
		# mid = left + (left + right) // 2
		# self._recursion(left, mid)
		# self._recursion(mid, right)
		self._recursion(numbers,left, right)
		return 


	def _recursion(self,numbers, left, right):
		## base case
		if left >= right:
			return 
		## when there are two elements
		if right - left == 1:
			## swap if left is larger than right
			if numbers[left] > numbers[right]:
				numbers[left], numbers[right] = numbers[right], numbers[left]
			return 

		mid = left + (left + right) // 2
		## Left
		self._recursion(numbers, left, mid)
		## Right
		self._recursion(numbers, mid+1, right)
		self.merge(numbers, left, mid, right)
		return

	def merge(self, numbers, left, mid, right):
		tem = [0] * (right - left + 1)
		i = 0
		j = mid + 1
		k = 0
		## When both left and right have element, merge them in order
		while i <= mid and j <= right:
			if numbers[i] < numbers[j]:
				tem[k] = numbers[i] 
				i += 1
				k += 1
			else:
				tem[k] = numbers[j]
				j += 1
				k += 1
		## Copy the leftover numbers directly if the other array is empty.
		while i <= mid:
			tem[k] = numbers[i]
			i += 1
			k += 1
		while j <= right:
			tem[k] = numbers[j]
			j += 1
			k += 1
		
		## Copy tem to numbers
		for i in range(left, right+1):
			numbers[i] = tem[i - left]
				

if __name__ == '__main__':
	array = [9,6,5,4,1]
	sort = MergeSort()
	sort.merge_sort(array)
	print(array)
