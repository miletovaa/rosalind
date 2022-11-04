# k-Mer Composition

# Given: A DNA string s in FASTA format (having length at most 100 kbp).
# Return: The 4-mer composition of s.

import itertools

with open('input/rosalind_kmer.txt') as fasta:
	for line in fasta:
		if 'Rosalind' in line:
			dna = ''
		else:
			dna += line.strip()

str = 'ACGT'

for x in itertools.product(*[str], repeat=len(str)):
	kmer = ''.join(x)
	num = i = 0
	for i in range(len(dna)):
		if dna[i:i+4] == kmer:
			num += 1
		i+=1
	print(num, end=' ')