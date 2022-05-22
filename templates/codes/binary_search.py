"""
Implement binary search
"""

def binary_search(nums, target, method='loop'):
	"""
	nums is an array of intergers (sorted from smallest to largest)
	return the index of target if target is in nums, return -1 otherwise.
	All intervals in implementations are in the form of [Left, right)
	"""
	## Edge case
	if not nums:
		return -1
	if method == 'loop':
		return loop(nums, target)
	elif method == 'recursion':
		return recursion(nums, target, 0, len(nums))

def recursion(nums, target, left, right):
	## Base case
	if left >= right:
		return - 1
	mid = left + (right - left) // 2
	if nums[mid] == target:
		return mid
	elif nums[mid] < target:
		left = mid + 1 
	else:
		right = mid
	return recursion(nums, target, left, right)


def loop(nums, target):
	left = 0
	right = len(nums)
	while left < right:
		mid = left + (right - left) // 2
		if nums[mid] == target:
			return mid 
		elif nums[mid] < target:
			left = mid + 1
		else: 
			right = mid
	return -1

if __name__ == '__main__':
	nums = [4]
	target = 3 
	method = 'recursion'
	rst = binary_search(nums, target, method=method)
	print(f'index of target is: {rst}')

