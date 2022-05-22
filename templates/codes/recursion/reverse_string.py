"""
Use recursion to reverse a string. Learn the call stack in VS Codes.
"""

def reverse_string(string):
	## Call recursively
	if string:
		return reverse_string(string[1:]) + string[0]
	## Base case
	else:
		return '' 
if __name__ == "__main__":
	string = 'abcd'
	print(reverse_string(string))