#!/usr/bin/env python3

def main():
	tmp = 1
	root = {}
	add_keyword(root,str(tmp))
	# Set highest power of 2 in dictionary to 2^800
	for i in range(800):
		tmp *= 2
		add_keyword(root,str(tmp))

	result = []
	T = int(input().strip())
	for i in range(T):
		result.append(find_keyword(root,input()))

	print('\n'.join(result))

def add_keyword(root, keyword):
	'''
		We add to the dictionary (aho-corasick tree) the keyword. At the last letter of the
		keyword we set a new value 'p' in the dictionary for us to know that at this depth
		of the tree this is a power of 2.
	'''
	length = len(keyword)
	node = root
	# Iterate through all characters
	for i in range(length):
		char = keyword[i]
		if char in node:
			node = node[char]
		elif(i < length):
			# if we are on the last character of the keyword flag it as a power of two
			if(i == length - 1):
				node[char] = {'p':''}
			# else move on to the next characters
			else:
				node[char] = {}
			node = node[char]

def find_keyword(root, keyword):
	'''
		We follow the letters of the string and for each occurence of the value 'p' we increment
		the counter of the powers of two that we find. After we repeat this procedure for each
		substring moving the starting index only.
	'''
	counter = 0
	length = len(keyword)
	for i in range(length):
		node = root
		for j in range(i,length):
			char = keyword[j]
			if char in node:
				node = node[char]
				if('p' in node):
					# The below three computations are different in performance. Need to check for best.  
					# counter = -~counter
					counter = counter + 1
					# counter += 1
			else:
				break
	return str(counter)
		
if __name__ == '__main__':
	main()
