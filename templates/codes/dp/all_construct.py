"""
This problem is similar to can_construct.py and count_construct.py.
Write a function that accepts a target string and an array of strings.
The function should return a 2D array cotaining ALL of the ways the 'target'
can be constructed by concatenating elements of the 'wordbank' array.Each 
element of the 2D array should represent one combination that constructs the 'target
You may reuse elements of 'wordbank' as many times as needed. 
Exampel:
	target = 'purple'
	wordbank = ['pur', 'p', 'ur', 'le', 'purpl']
	return [['pur','p', 'le'], ['p', 'ur', 'p', 'le']]
"""
import copy
#### Backtracking?
def all_construct(target, wordbank, method='tabular'):
	if method == 'recursion':
		rst = []
		running_state = []
		memo = set()
		_ = recursion(rst, target, wordbank,running_state, memo) 
		return rst
	else:
		rst = tabular(target, wordbank)
		if rst:
			return rst
		else:
			return []

def recursion(rst, remain, wordbank, running_state, memo):
	## Base case:
	if not remain:
		rst.append(running_state)
		return True
	if remain in memo:
		return False
	for word in wordbank:
		## Make a copy of state
		copy_state = running_state[:]
		if word == remain[:len(word)]:
			copy_state.append(word)
			found = recursion(rst, remain[len(word):], wordbank, copy_state, memo)
			if found:
				return

	# when reaching this point, the remain will not be recuded. put it in memo. 
	memo.add(remain)
	return 

def tabular(target, wordbank):
	table = [[] for _ in range(1 + len(target))]#(1 + len(target))
	table[0].append([])
	for i in range(len(table)):
		for word in wordbank:
			if table[i]:
				start_index = i 
				end_index = i + len(word)
				if word == target[start_index:end_index] and end_index < len(table):
					if table[start_index]:
						#tem = [t.append(word) for t in table[start_index]]
						tem = copy.deepcopy(table[start_index])
						for j in range(len(tem)):
							tem[j].append(word)
					else:
						tem = [[word]]
					for t in tem:
						table[end_index].append(t)
	return table[-1]



if __name__ == '__main__':
	target = 'purple'
	wordbank = ['pur', 'p', 'ur', 'le', 'purpl']
	#Expected output: [['pur','p', 'le'],['p', 'ur', 'p', 'le']]
	print(all_construct(target, wordbank)) 
	target = 'abcdef'
	wordbank = ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']
	# Expected output: [['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'],['abcd', 'ef']]
	print(all_construct(target, wordbank)) 
	target = 'skateboard'
	wordbank=['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']
	# Expected output: []
	print(all_construct(target, wordbank)) 
	target = 'eeeeeeeeeeeeeeeeeeeeeeeeeef'
	wordbank = ['e', 'ee', 'eee', 'eeee', 'eeeee']
	# Expected output : []
	print(all_construct(target, wordbank))
	print("Done")