#!/usr/bin/env python3

def main():
	tmp = 1
	root = {}
	add_keyword(root,str(tmp))
	for i in range(800):
		tmp *= 2
		add_keyword(root,str(tmp))

	result = []
	T = int(input().strip())
	for i in range(T):
		result.append(find_keyword(root,input()))

	print('\n'.join(result))

def add_keyword(root, keyword):
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
	counter = 0
	length = len(keyword)
	for i in range(length):
		node = root
		for j in range(i,length):
			char = keyword[j]
			if char in node:
				node = node[char]
				if('p' in node):
					# counter = -~counter
					counter = counter + 1
					# counter += 1
			else:
				break
	return str(counter)
		
if __name__ == '__main__':
	main()
