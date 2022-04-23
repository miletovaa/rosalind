# Finding a Spliced Motif

# Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
# Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one

s = []
l = ''
with open('input/rosalind_sseq.txt') as fasta:
    for line in fasta:
        if 'Rosalind' in line:
            if l != '': s.append(l)
            l = ''
        else:
            l += line.strip()
    s.append(l)

start = 0
nums = []
for l in s[1]:
	start = s[0].find(l, start+2)
	nums.append(str(start+1))

print(' '.join(nums))