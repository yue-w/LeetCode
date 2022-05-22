"""
Write a function 'how_sum(target_sum, numbers)' that takes in a targetSum and an 
array of positive numbers as arguments. 
The function should return an array containing any combination of elements that
add up to exactly the traget_sum. elements can be used multiple times.
If there is no combination that adds up to the target_sum, return None. 
If there are multiple combinations that add up to the target_sum, return any single one. 
"""
#%%
def how_sum(target_sum, numbers, method='tabluar'):
	if method == 'recursion':
		memo = {}
		return recursion(target_sum, numbers, memo)
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
	for num in numbers:
		remainder = target_sum - num
		rst = recursion(remainder, numbers, memo)
		if isinstance(rst, list):
			rst.append(num)
			return rst
	memo[target_sum] = None
	return None

def tabular(target_sum, numbers):
	table = [None] * (target_sum + 1)
	table[0] = []
	for i in range(len(table)):
		if table[i] is not None:
			for num in numbers:
				index = num + i 
				if index <= target_sum:
					running_lst = table[i][:]
					running_lst.append(num)
					table[index] = running_lst

	return table[-1]

if __name__ == "__main__":
	assert how_sum(7, [2, 3]) is not None, 'error'
	assert how_sum(7, [5, 3, 4, 7]) is not None, 'error'
	assert how_sum(7, [2, 4]) is None, 'error'
	assert how_sum(8, [2, 3, 5]) is not None, 'error'
	assert how_sum(7, [3, 3, 5]) is None, 'error'
	assert how_sum(300, [7, 14]) is None, 'error'
	print('All test passed')
	
# %%
