"""
Write a function that accepts a target string and an array of strings.
The function should return a boolean indicating whether or not the 'target'
can be constructed by concatenating elements of the 'wordbank' array.
You may reuse elements of 'wordbank' as many times as needed. 
Example 1: target: 'abcdef', wordbank=['ab', 'abc', 'cd', 'def', 'abcd']
Return True, because 'abcdef' = 'abc' + 'def'
Example 2: target: 'skateboard', wordbank=['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']
Return False.
"""

def can_construct(target, wordbank, method='tablular'):

	if method == 'recursion':
		memo = set()
		return recursion(target, wordbank, memo)
	else:
		return tabular(target, wordbank)

def recursion(remain_word, wordbank, memo):
	## Base case 
	if not remain_word:
		return True 
	
	## Memoization check.
	if remain_word in memo:
		return False
	
	## Remove prefix using word from the wordbank
	for word in wordbank:
		### if has prefix, remove the prefix then keep recursing
		if word == remain_word[0:len(word)]:
			rst = recursion(remain_word[len(word):], wordbank, memo)
			if rst:
				return True
	## Memoization update. 
	memo.add(remain_word)
	return False

def tabular(target, wordbank):
	table = [False] * (len(target) + 1)
	table[0] = [True]
	for i in range(len(table)):
		if table[i]:
			for word in wordbank:
				end_index = i  + len(word)
				if word == target[i:end_index]:
					table[end_index] = True
					if end_index == len(target):
						return True

	return table[-1]

if __name__ == '__main__':
	target = 'abcdef'
	wordbank = ['ab', 'abc', 'cd', 'def', 'abcd']
	assert can_construct(target, wordbank) 
	target = 'skateboard'
	wordbank=['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']
	assert not can_construct(target, wordbank) 
	target = 'enterapotentpot'
	wordbank = ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']
	assert can_construct(target, wordbank) 
	target = 'eeeeeeeeeeeeeeeeeeeeeeeeeef'
	wordbank = ['e', 'ee', 'eee', 'eeee', 'eeeee']
	assert not can_construct(target, wordbank) 
	print('All test passed')



		



			


