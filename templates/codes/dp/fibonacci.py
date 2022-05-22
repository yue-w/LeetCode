


from tkinter import N


def fib_bottom_up(n):
	if n < 3:
		return 1
	a = 1
	b = 1
	for _ in range(n-3):
		a, b = b, a + b
	return a + b

def fib_top_bottom(n, seen=None):
	if n < 3:
		return 1
	if n in seen:
		return seen[n] 
	seen[n] = fib_top_bottom(n-1, seen) + fib_top_bottom(n-2, seen)
	return seen[n]
# %%
if __name__ == '__main__':
	seen = {}
	fib = fib_bottom_up(50)
	#fib = fib_top_bottom(50, seen)
	print(fib)