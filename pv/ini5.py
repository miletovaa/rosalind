# Working with Files

# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

file = open('rosalind_ini5.txt', 'r')
new = open('rosalind_ini5_output.txt', 'w')

i = 0

for line in file:
	if i%2==1:
		new.write(line)
		# print(line)
	i=i+1