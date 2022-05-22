"""
Write a function 'best_sum(target_sum, numbers)' that takes in a targetSum and an 
array of positive numbers as arguments. 
The function should return an array containing the shortest combination of numbers 
that add up to exactly the traget_sum. Elements can be used multiple times.
If there is a tie for the shortest combination, you may return any one of the shortest.
"""

def best_sum(target_sum, numbers, method='recursion'):
	if method == 'recursion':
		memo = {}
		return  recursion(target_sum, numbers, memo)
	else:
		return tabular(target_sum, numbers)


def recursion(target_sum, numbers,memo):
	## Base case 1
	if target_sum == 0:
		memo[0] = []
		return []
	## Base case 2
	if target_sum < 0:
		memo[target_sum] = None
		return None 
	## Check memoization
	if target_sum in memo:
		return memo[target_sum]
	## recursion
	rst = None
	rst_len = float('inf')
	num_run = None
	for num in numbers:
		remainder = target_sum - num
		rst_run = recursion(remainder, numbers, memo)
		## Get the shortest
		if isinstance(rst_run, list):
			# if find a solution, keep the shortest.
			if len(rst_run) < rst_len:
				rst = rst_run[:] 
				rst_len = len(rst_run)
				num_run = num
	## if find a solution, add the current number into the list
	if isinstance(rst, list) and num_run: 
		rst.append(num_run)
	memo[target_sum] = rst
	return rst

def tabular(target_sum, numbers):
	table = [None] * (target_sum + 1) 
	table[0] = []
	for i in range(len(table)):
		if table[i] is not None:
			for num in numbers:
				tem = table[i][:]
				index = i + num
				if index <= target_sum:
					tem.append(num)
					if table[index] is None:
						table[index] = tem
					elif len(tem) < len(table[index]):
						table[index] = tem
	return table[-1]


if __name__ == "__main__":
	print(best_sum(7, [2, 3]))
	print(best_sum(7, [5, 3, 4, 7]))
	print(best_sum(100, [1, 2, 5, 25]))
	print(best_sum(8, [1, 2, 4]))
	