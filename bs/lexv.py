# Ordering Strings of Varying Length Lexicographically

# Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n≤4).
# Return: All strings of length at most n formed from A, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)

import itertools

inp = 'M Y S W B G X H D N'
str = inp.replace(' ', "")

length = 10

for i1 in range(length):
	print(str[i1])
	for i2 in range(length):
		print(str[i1] + str[i2])
		for i3 in range(length):
			print(str[i1] + str[i2] + str[i3])