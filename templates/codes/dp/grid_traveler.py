"""
A traveler on a 2D grid. You begin in the top-left corner and the goal is to travel 
to the bottom-right corner. You can only travel down or right. In how many ways 
can you travel to the goal on a grid with dimension m*n? 
"""
#%%
def gird_traveler_bottom_up(m, n):
	assert m >=2 and n>= 2
	## Initialize a table. Top-left (0, 0), bottom right (m-1, n-1)
	table = [[0 for c in range(n)] for r in range(m)]
	# ## Set values to the last column.
	# table[:, n - 1] = [v -1 for v in range(n-1, -1, -1)]
	# ## Set values to the last row.
	# table[0, m - 1] = [v -1 for v in range(m-1, -1, -1)]
	for v in range(0, m-1):
		table[v][n - 1] = 1
	for v in range(0, n-1):
		table[m - 1][v] = 1
	for row in range(m-2, -1, -1):
		for col in range(n-2, -1, -1):
			## sum of the cell below and the cell on the right
			table[row][col] = table[row+1][col] + table[row][col+1]

	return table[0][0]

def gird_traveler_top_bottom(m, n):
	## Initialize a table to store seen state. -1 for unseen state.
	table = [[-1 for _ in range(n)] for _ in range(m)]

	return recursion(0, 0, m, n, table) 

def recursion(row, col, m, n, table):
	## Base case
	if row == m-1 or col == n-1:
		table[row][col] = 1
		return 1
	## If the value of the cell is >0, it means we have seen the cell
	if table[row][col] > 0:
		return table[row][col]
	table[row][col] = recursion(row+1, col, m, n, table) + recursion(row, col+1, m, n, table)
	return table[row][col]
#%%
if __name__ == '__main__':
	#rst = gird_traveler_bottom_up(18,18)
	rst = gird_traveler_top_bottom(18,18)
	print(rst)
# %%
