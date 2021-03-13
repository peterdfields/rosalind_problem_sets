#!/usr/bin/env python
 
def get_palindromes(str):
	""" Return all palindromes in str of minimum size 3 """
	length = len(str) + 1
	found = []
	pos = []
	for i in xrange(0, length):
		for j in xrange(i+2, length):
			mid = i + ((j - i) / 2)
			if str[i:mid] == str[mid+1:j][::-1]: # In-efficient
				y = x[i:j]
				found.append(str[i:j])
				pos.append(y)
	return found
	return pos
 
if __name__ == '__main__':
	x = str('efeababaf')
	print get_palindromes(x)
