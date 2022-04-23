# Locating Restriction Sites


# Given: A DNA string of length at most 1 kbp in FASTA format.
# Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

def is_palindrome(string):
	second = ''
	for nt in string:
		match nt:
			case 'A':
				second += 'T'
			case 'G':
				second += 'C'
			case 'C':
				second += 'G'
			case 'T':
				second += 'A'
	reversed_string = second[::-1]
	if string == reversed_string:
		return True
	else:
		return False

str = ''
with open('input/rosalind_revp.txt') as fasta:
	for line in fasta:
		if 'Rosalind' not in line:
			str += line.strip()

i = 0
while i < len(str):
	n = 3
	if len(str) - i >= 12 :
		max_l = 12
	else:
		max_l = len(str) - i
	while n <= max_l:
		if is_palindrome(str[i:i+n]) == True:
			print(i+1, n)
		n+=1
	i+=1