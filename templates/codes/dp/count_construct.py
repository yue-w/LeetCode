"""
This problem is similar to can_construct.py.
Write a function that accepts a target string and an array of strings.
The function should return the total number of ways the 'target'
can be constructed by concatenating elements of the 'wordbank' array.
You may reuse elements of 'wordbank' as many times as needed. 
Example 1: target: 'abcdef', wordbank=['ab', 'abc', 'cd', 'def', 'abcd']
Return 1, because 'abcdef' = 'abc' + 'def'
Example 2: target: 'skateboard', wordbank=['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']
Return 0.
"""

def count_construct(target, wordbank, method='tabular'):
	if method == "method":
		memo = set()
		return recursion(target, wordbank, memo) 
	else:
		return tabular(target, wordbank)

def recursion(remain, wordbank, memo):
	## Base case
	if not remain:
		return 1
	if remain in memo:
		return 0
	running_sum = 0
	for word in wordbank:
		if word == remain[:len(word)]:
			running_sum += recursion(remain[len(word):], wordbank, memo)
	if running_sum == 0:
		memo.add(remain)
	return running_sum

def tabular(target, wordbank):
	table = [0] * (len(target) + 1) 
	table[0] = 1
	for i in range(len(table)):
		if table[i]:
			for word in wordbank:
				start_index = i 
				end_index = i + len(word)
				if target[start_index:end_index] == word:
					table[end_index] += table[start_index]

	return table[-1]

if __name__ == '__main__':
	target = 'purple'
	wordbank = ['purp', 'p', 'ur', 'le', 'purpl']
	assert count_construct(target, wordbank) == 2
	target = 'abcdef'
	wordbank = ['ab', 'abc', 'cd', 'def', 'abcd']
	assert count_construct(target, wordbank) == 1
	target = 'skateboard'
	wordbank=['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']
	assert count_construct(target, wordbank) == 0
	target = 'enterapotentpot'
	wordbank = ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'] 
	assert count_construct(target, wordbank)  == 4
	target = 'eeeeeeeeeeeeeeeeeeeeeeeeeef'
	wordbank = ['e', 'ee', 'eee', 'eeee', 'eeeee']
	assert count_construct(target, wordbank) == 0
	print('All tests passed')