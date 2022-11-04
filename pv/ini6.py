# Dictionaries

# Given: A string s of length at most 10000 letters.
# Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

string = open('rosalind_ini6.txt', 'r')

with string as inp:
	array = inp.read().split()

dict = {}

for word in array:
	if word in dict:
		dict[word]=dict[word]+1
	else:
		dict[word]= 1

for key, value in dict.items():
    print(key, value)