# Finding a Motif in DNA

# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

string = 'GATATATGCATATACTT'
str = 'ATAT'

x = index = 0

while index != -1 :
	index = string.find(str, x)
	if index != -1:
		index += 1
		x = index
		print(index, end=" ")