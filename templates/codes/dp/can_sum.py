"""
Write a function 'can_sum(target_sum, numbers)' that takes in a target_sum (integer) and an 
array of positive integers as arguments. 
The function should return a boolean indicating whether or not it is possible to 
generate the target_sum using numbers from the array.
You may use an element of the array as many times as needed.
You may assume that all input numbers are nonnegative.
"""
def can_sum(target_sum, numbers, method='table'):
	if method == 'recursion':
		memo = {}
		min_num = min(numbers)
		return recursion(target_sum, numbers, min_num, memo)
		
	else: 
		return tabular(target_sum, numbers)

def recursion(target_sum, numbers, min_num,memo=None):
	## Base case
	if target_sum == 0:
		memo[0] = True
		return True 
	if target_sum < min_num or  target_sum < 0: #
		memo[target_sum] = False
		return  False
	## memoization: if target_sum has been seen and is True, return True.
	if target_sum in memo:
		return memo[target_sum]
	for num in numbers:
		remainder = target_sum-num
		rst = recursion(remainder, numbers, min_num, memo)
		if rst == True:
			memo[remainder] = True
			return True
	memo[target_sum] = rst
	return False

def tabular(target_sum, numbers):
	table = [False] * (target_sum + 1)
	table[0] = True 
	for i in range(len(table)):
		## if table[i] is True, it means this number can be constructed,
		## we then add other numbers to this number to update the table
		if table[i]:
			for num in numbers:
				index = i + num
				if index < len(table):
					table[index] = True
	return table[-1]


if __name__ == '__main__':
	target_sum = 7
	numbers = [2, 3]
	assert can_sum(target_sum, numbers) == True 
	target_sum = 7
	numbers = [5, 3, 4, 7]
	assert can_sum(target_sum, numbers) == True 
	target_sum = 7
	numbers = [2, 4]
	assert can_sum(target_sum, numbers) == False 
	target_sum = 8
	numbers = [2, 3, 5]
	assert can_sum(target_sum, numbers) == True 
	target_sum = 300
	numbers = [7, 14]
	assert can_sum(target_sum, numbers) == False
	print("All tests passed") 