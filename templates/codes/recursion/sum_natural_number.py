
def sum_natural_number(n):
	"""
	n is a natural number, return 1 + 2 + ... + n
	"""
	assert isinstance(n, int) and n > 0
	## base case
	if n == 1:
		return 1
	return n + sum_natural_number(n - 1)

if __name__ == "__main__":
	print(sum_natural_number(7))