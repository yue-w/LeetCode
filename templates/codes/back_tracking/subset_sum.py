"""
Given an array of positive integers and a target number. Return 
all possible sub sets of this array that satisfies the following requirement:
from the array if the numbers sums to the target number. Return None if no such
the numbers in each of the sub set sum to the target number. 
Subsets can be any order.
Example: input array = [5, 10, 12, 13, 15, 18]. target number: 30. 
return [[5, 10, 15], [5, 12, 13], [12, 18]]
"""


def sub_set_sum(nums, target):
	rst = []
	current_nums = []
	depth = 0
	recursion(rst, nums, target, depth, current_nums)

	if rst:
		return rst 
	else:
		return None


def recursion(rst, nums, target, depth, current_nums):
	running_sum = sum(current_nums) 
	## Base case: if the running sum is target, return
	if running_sum == target:
		rst.append(current_nums)
		return 
	## Base case: if the running sum is larger than target, return
	if running_sum > target:
		return 
	## Base case: if there is no number left
	if depth == len(nums):
		return
	
	## keep recursing
	## left tree: use the number of the current depth
	state_backtrack = current_nums[:]
	current_nums.append(nums[depth])
	recursion(rst, nums, target, depth+1, current_nums)
	## right tree: do not use the number of the current depth
	recursion(rst, nums, target, depth+1, state_backtrack)

if __name__ == '__main__':
	nums =  [5, 10, 12, 13, 15, 18]
	target = 30
	rst = sub_set_sum(nums, target)
	print(rst)

	
	
	 