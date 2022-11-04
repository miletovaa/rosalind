# RNA Splicing

# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
# Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

key = 0
dict = {}
with open('input/rosalind_splc.txt') as fasta:
    for line in fasta:
        if len(line) > 1:
            if 'Rosalind' in line:
                key += 1
                dict[key] = ""
            else:
                dict[key] += line.strip()
dna = dict.pop(1)

def cleanLine(key):
	if dict[key] in dna:
		return False
	else:
		return True

for key in dict:
	while cleanLine(key) == False:
		dna = dna.replace(dict[key], '')

codons_str = dna.replace('T', 'U')

codon_to_amino = {
	'UUU': 'F', 	'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
	'UUC': 'F', 	'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
	'UUA': 'L', 	'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
	'UUG': 'L', 	'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
	'UCU': 'S', 	'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
	'UCC': 'S', 	'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
	'UCA': 'S', 	'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
	'UCG': 'S', 	'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
	'UAU': 'Y', 	'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
	'UAC': 'Y', 	'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
	'UAA': 'Stop',  'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
	'UAG': 'Stop',  'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
	'UGU': 'C', 	'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
	'UGC': 'C', 	'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
	'UGA': 'Stop',  'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
	'UGG': 'W', 	'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}

codon = aminos_str = ''
i = 1
for l in codons_str:
	if i%3 == 0:
		codon += l
		if codon_to_amino[codon] != 'Stop':
			aminos_str += codon_to_amino[codon]
		codon = ''
	else:
		codon += l
	i+=1

print(aminos_str)