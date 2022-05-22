"""
Convert a decimal number to a binary number, use recursion. 
"""

from math import remainder


def decimal_to_binary(num):
	## Base case
	if num == 0:
		return ''
	## Recursion
	remainder = num % 2
	return decimal_to_binary(num // 2) +  str(remainder)

if __name__ == "__main__":
	num = 7
	print(f'Binary value of {num} is {decimal_to_binary(num)}')
