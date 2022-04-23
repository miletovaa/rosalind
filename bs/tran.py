# Transitions and Transversions

# Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
# Return: The transition/transversion ratio R(s1,s2).

s = []
l = ''
with open('input/rosalind_tran.txt') as fasta:
    for line in fasta:
        if 'Rosalind' in line:
            if l != '': s.append(l)
            l = ''
        else:
            l += line.strip()
    s.append(l)

letters = {'A':'G','G':'A','C':'T','T':'C'}
transition = transversion = x = 0
while x < len(s[0])-1:
	if s[0][x] != s[1][x]:
		if s[1][x] == letters[s[0][x]]:
			transition += 1
		else:
			transversion += 1
	x+=1

print(transition / transversion)